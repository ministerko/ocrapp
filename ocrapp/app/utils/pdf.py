import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io

# Update this path to your Tesseract executable if needed
pytesseract.pytesseract.tesseract_cmd = r'/tesseract'

def extract_text_from_pdf(pdf_path: str) -> str:
    document = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        
        # Extract text directly from the PDF page
        text += page.get_text()
        
        # Extract images from the PDF page
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Open image with PIL and perform OCR
            image = Image.open(io.BytesIO(image_bytes))
            text += pytesseract.image_to_string(image) + "\n"

    return text
