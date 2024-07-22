# 🖼️📄 OCR Text Extraction App

Welcome to the **OCR Text Extraction App**! This application allows users to extract text from image files, PDFs, and DOCX documents. With a simple and intuitive interface, users can upload their files, view the extracted text, and download it in text format.

## 🚀 Features

- **Upload Files:** Supports images, PDFs, and DOCX files.
- **Text Extraction:** Extracts text from uploaded files.
- **Text Display:** View the extracted text in a user-friendly interface.
- **Download Text:** Save the extracted text as a `.txt` file.
- **Clear Text:** Remove text and start a new extraction process.

## 📦 Installation

To get started with this project, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ocrapp.git
cd ocrapp
```

### 2. Create a Virtual Environment

```bash
python -m venv ocrvenv
source ocrvenv/bin/activate  # On Windows use `ocrvenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python -c "from app.database import create_db_and_tables; create_db_and_tables()"
```

## 🔧 Usage

### Start the Server

```bash
uvicorn app.main:app --reload
```

Open your browser and go to `http://127.0.0.1:8000` to access the application.

### Upload a File

1. **Drag and Drop** or **Click** to upload an image, PDF, or DOCX file.
2. Wait for the text extraction to complete.
3. **View** the extracted text in the display area.
4. **Download** the text file using the download button.
5. **Clear** the text area if needed.

## 🧪 Running Tests

To ensure everything is working correctly, run the tests:

```bash
pytest
```

## 🛠️ Development

- **Backend:** FastAPI for API development, SQLAlchemy for database interaction.
- **Database:** SQLite for local storage.
- **Testing:** Pytest for testing.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or suggestions, feel free to reach out:

- **Email:** mwaijegakelvin@gmail.com
- **GitHub:** [your-username](https://github.com/ministerko)

Happy coding! 🚀
