# fastapi_project

This project is a backend service built with **FastAPI** that uses **Optical Character Recognition (OCR)** to extract text from image and PDF files. The OCR processing is done using **Tesseract** via **pytesseract**, and the API allows users to upload files and get the extracted text in JSON format.

## Features

- **OCR API**: Supports image files (`.jpg`, `.jpeg`, `.png`) and PDF files.
- **FastAPI Framework**: Lightweight and high-performance API.
- **Dockerized**: Easily deployable using Docker.
- **JSON Response**: Extracted text is returned in a simple JSON format.

## Tech Stack

- **FastAPI**: The web framework for building APIs.
- **Pytesseract**: Python wrapper for Tesseract OCR.
- **Pillow**: Image processing library.
- **pdf2image**: Converts PDF files to images.
- **Docker**: Used to containerize the application.

## Requirements

- **Python 3.10+**
- **Tesseract OCR**
- **Docker** (optional, for containerization)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Haileliul/fastapi_project.git
cd fastapi_project
```
### 2. Set Up a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```
### 4. running the app 

```bash
uvicorn main:app --reload
```
