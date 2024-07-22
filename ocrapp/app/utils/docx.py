import docx

def extract_text_from_docx(docx_path: str) -> str:
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text
