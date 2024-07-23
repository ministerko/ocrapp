import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import docx
import cv2
import numpy as np

# Preprocessing functions
def get_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image: np.ndarray) -> np.ndarray:
    """Apply binary thresholding to image."""
    return cv2.threshold(image, 100, 160, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

def denoise(image: np.ndarray) -> np.ndarray:
    """Remove noise from image."""
    return cv2.fastNlMeansDenoising(image, None, 30, 7, 21)

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """Preprocess image by applying grayscale conversion, thresholding, and denoising."""
    gray = get_grayscale(image)
    binary = thresholding(gray)
    denoised = denoise(binary)
    return denoised

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF, handling both typed and scanned PDFs."""
    extracted_text = ""
    pdf_document = fitz.open(file_path)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Extract text directly if available
        text = page.get_text()
        if text:
            extracted_text += text
        
        # Extract images and perform OCR if images are present
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            
            # Convert image to numpy array for preprocessing
            image_np = np.array(image)
            processed_image = preprocess_image(image_np)
            
            # Convert processed image back to PIL Image for pytesseract
            processed_image_pil = Image.fromarray(processed_image)
            
            # Extract text from image
            extracted_text += pytesseract.image_to_string(processed_image_pil)
    
    return extracted_text

def extract_text_from_file(file_path: str) -> str:
    """Extract text from various file types."""
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        # Handle image files
        image = Image.open(file_path)
        image_np = np.array(image)
        processed_image = preprocess_image(image_np)
        processed_image_pil = Image.fromarray(processed_image)
        return pytesseract.image_to_string(processed_image_pil)
    
    elif file_path.lower().endswith('.pdf'):
        # Handle PDF files (both typed and scanned)
        return extract_text_from_pdf(file_path)

    elif file_path.lower().endswith('.docx'):
        # Handle DOCX files
        doc = docx.Document(file_path)
        extracted_text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        return extracted_text

    else:
        raise ValueError("Unsupported file type")
