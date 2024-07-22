import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_extract_text(setup_db):
    image_path = os.path.join(os.path.dirname(__file__), "images", "test.png")

    with open(image_path, "rb") as image_file:
        response = client.post("/extract-text/", files={"file": ("test.png", image_file, "image/png")})
    
    assert response.status_code == 200
    assert "extracted_text" in response.json()
