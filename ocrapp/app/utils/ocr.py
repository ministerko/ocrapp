import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import docx
import cv2
import numpy as np

# Preprocessing functions
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

def denoise(image):
    return cv2.fastNlMeansDenoising(image, None, 30, 7, 21)



def preprocess_image(image):
    gray = get_grayscale(image)
    binary = thresholding(gray)
    denoised = denoise(binary)
    return denoised

def extract_text_from_file(file_path: str) -> str:
    # Determine file type from the file extension
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Open image file
        image = Image.open(file_path)
        
        # Convert image to numpy array for preprocessing
        image_np = np.array(image)
        processed_image = preprocess_image(image_np)
        
        # Convert processed image back to PIL Image for pytesseract
        processed_image_pil = Image.fromarray(processed_image)
        
        # Extract text
        return pytesseract.image_to_string(processed_image_pil)
    
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
