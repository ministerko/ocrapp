from PIL import Image

def save_image(file) -> str:
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return file_location
