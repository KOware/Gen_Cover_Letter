import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))

def generate_cover_letter(resume_text: str, job_posting: dict) -> str:
    """Generate a tailored cover letter using resume text and job description.
    
    Args:
        resume_text: Extracted resume string
        job_posting: Dictionary with job title, company, description
    
    Returns:
        A cover letter as a string
    """
    prompt = f"""
You are a job application assistant. Write a personalized, professional cover letter based on the following:

Resume:
{resume_text}

Job Title: {job_posting['title']}
Company: {job_posting['company']}
Job Description: {job_posting['description']}

Only return the cover letter. Do not include explanations or formatting hints.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
