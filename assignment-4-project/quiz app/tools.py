import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text: str) -> str:
    """Summarizes the given text using Gemini."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(f"Summarize the following text:\n\n{text}")
    return response.text

def generate_quiz(text: str) -> str:
    """Generates a quiz from the given text using Gemini."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(f"Generate a multiple-choice quiz from the following text:\n\n{text}")
    return response.text

