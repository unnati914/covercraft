import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def generate_cover_letter(model, resume_text, job_description):
    prompt = f"""
Write a concise, enthusiastic, and professional cover letter based on this resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

Tone: Confident, clear, and personalized.
Length: Under 300 words.
"""
    response = model.generate_content(prompt)
    return response.text
