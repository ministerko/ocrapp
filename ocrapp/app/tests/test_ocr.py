# app/tests/test_ocr.py

from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_extract_text():
    # Define the path to the test image
    image_path = os.path.join(os.path.dirname(__file__), "images", "test.png")
    
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Send the POST request with the image file
        response = client.post("/extract-text/", files={"file": ("test.png", image_file, "image/png")})
    
    # Perform assertions on the response
    assert response.status_code == 200
    assert "extracted_text" in response.json()
