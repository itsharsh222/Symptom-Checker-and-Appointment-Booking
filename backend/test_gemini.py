import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

try:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content("Hello, can you help me?")
    print("SUCCESS:", response.text)
except Exception as e:
    print("ERROR:", str(e))