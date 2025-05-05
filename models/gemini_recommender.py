import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env file.")

# Configure Gemini client
genai.configure(api_key=api_key)

def generate_recommendation(ticker, max_price, min_price, average_price, predicted_price):
    try:
        prompt = (
            f"Market Insight: The stock {ticker} has shown historical volatility. "
            f"Maximum Close: ${max_price:.2f}, Minimum Close: ${min_price:.2f}, "
            f"Average Close: ${average_price:.2f}. "
            f"The LSTM model predicts the next close will be ${predicted_price:.2f}. "
            f"Based on this, provide a concise investment recommendation for this stock, "
            f"assuming a medium risk tolerance."
        )

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Gemini API failed: {e}"
