# app/utils/ocr.py

from PIL import Image
import pytesseract
from fastapi import UploadFile
import io

def extract_text_from_file(file: UploadFile) -> str:
    image = Image.open(io.BytesIO(file.file.read()))
    return pytesseract.image_to_string(image)
