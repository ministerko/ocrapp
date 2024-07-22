import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import docx

def extract_text_from_file(file_path: str) -> str:
    # Determine file type from the file extension
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Handle image files
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    
    elif file_path.lower().endswith('.pdf'):
        # Handle PDF files
        extracted_text = ""
        pdf_document = fitz.open(file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            extracted_text += page.get_text()
        return extracted_text

    elif file_path.lower().endswith('.docx'):
        # Handle DOCX files
        doc = docx.Document(file_path)
        extracted_text = ""
        for paragraph in doc.paragraphs:
            extracted_text += paragraph.text + "\n"
        return extracted_text

    else:
        raise ValueError("Unsupported file type")

