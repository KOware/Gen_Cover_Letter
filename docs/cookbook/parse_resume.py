from pdfminer.high_level import extract_text

def parse_resume(resume_path: str) -> str:
    """Extract plain text from a resume PDF file.
    
    Args:
        resume_path: Path to the resume PDF file
    
    Returns:
        Extracted text as a string
    """
    try:
        return extract_text(resume_path).strip()
    except Exception as e:
        return f"Error parsing resume: {str(e)}"
