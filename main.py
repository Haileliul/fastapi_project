from fastapi import FastAPI, UploadFile, File, HTTPException
from pytesseract import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import io

app = FastAPI()

# Configure path to tesseract executable (needed for Windows users)
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    try:
        # Read the file content
        contents = await file.read()
        
        # Determine if it's an image or a PDF
        if file.content_type in ["image/jpeg", "image/png", "image/jpg"]:
            # Open the image file and run OCR
            image = Image.open(io.BytesIO(contents))
            text = pytesseract.image_to_string(image)
        elif file.content_type == "application/pdf":
            # Convert PDF to image
            images = convert_from_bytes(contents)
            text = ""
            for image in images:
                # Extract text from each page
                text += pytesseract.image_to_string(image) + "\n"
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        return {"extracted_text": text.strip()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
