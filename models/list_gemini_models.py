import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Missing GOOGLE_API_KEY in .env file.")

# ✅ Configure Gemini client
genai.configure(api_key=api_key)

# ✅ List and display all available models
try:
    models = genai.list_models()
    print("\n📄 Available Gemini Models:\n")
    for model in models:
        print(f"🧠 Model ID: {model.name}")
        print(f"   Description: {model.description}")
        print(f"   Input Token Limit: {model.input_token_limit}")
        print(f"   Output Token Limit: {model.output_token_limit}")
        print(f"   Supported Generation Methods: {model.supported_generation_methods}")
        print("-" * 60)
except Exception as e:
    print(f"❌ Failed to list models: {e}")
