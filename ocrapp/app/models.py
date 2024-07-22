from sqlmodel import SQLModel, Field
from typing import Optional

class OCRRequest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    extracted_text: Optional[str] = None
