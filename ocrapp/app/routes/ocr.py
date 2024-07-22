from fastapi import APIRouter, UploadFile, File
from sqlmodel import Session
from pathlib import Path
from ..database import engine
from ..models import OCRRequest
from ..utils.ocr import extract_text_from_file  # Ensure this function is used if the correct import was done

router = APIRouter()

@router.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    # Ensure the directory exists
    upload_dir = Path("files")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    # Define the file path
    file_location = upload_dir / file.filename
    
    # Save the uploaded file
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    # Extract text from the saved file
    extracted_text = extract_text_from_file(str(file_location))

    # Create and save the OCR request record
    ocr_request = OCRRequest(file_path=str(file_location), extracted_text=extracted_text)
    with Session(engine) as session:
        session.add(ocr_request)
        session.commit()
        session.refresh(ocr_request)

    # Optional: Clean up the uploaded file after processing
    file_location.unlink()
    
    return ocr_request
