# models/gemini_recommender.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env file.")

genai.configure(api_key=api_key)

def generate_recommendation(ticker, max_price, min_price, average_price, predicted_price):
    prompt = (
        f"Provide a brief stock recommendation for ticker {ticker}.\n"
        f"Max price: ${max_price:.2f}, Min price: ${min_price:.2f}, "
        f"Average price: ${average_price:.2f}, Predicted next close: ${predicted_price:.2f}."
    )
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API failed: {e}"
