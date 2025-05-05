import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
try:
    models = genai.list_models()
    print("✅ Available Gemini Models:")
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print("❌ Error:", e)