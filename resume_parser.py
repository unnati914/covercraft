import pdfplumber

def extract_text_from_resume(uploaded_file):
    """
    Extracts and returns the full text from a PDF resume.
    """
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join(
                page.extract_text() for page in pdf.pages if page.extract_text()
            )
        return text
    except Exception as e:
        return f"Error reading resume: {e}"
