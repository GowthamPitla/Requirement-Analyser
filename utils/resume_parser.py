
import PyPDF2

def parse_resume(uploaded_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
    return text.lower()
