from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlmodel import Session
from pathlib import Path
from ..database import engine
from ..models import OCRRequest
from ..utils.ocr import extract_text_from_file  # Ensure this function is used if the correct import was done
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    upload_dir = Path("files")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    file_location = upload_dir / file.filename
    
    try:
        # Save the uploaded file
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        
        # Extract text from the saved file
        extracted_text = extract_text_from_file(str(file_location))
        
        if not extracted_text:
            logger.warning(f"No text extracted from file: {file.filename}")

        # Create and save the OCR request record
        ocr_request = OCRRequest(file_path=str(file_location), extracted_text=extracted_text)
        with Session(engine) as session:
            session.add(ocr_request)
            session.commit()
            session.refresh(ocr_request)
        
        # Optional: Clean up the uploaded file after processing
        file_location.unlink()

        return ocr_request
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the file.")

