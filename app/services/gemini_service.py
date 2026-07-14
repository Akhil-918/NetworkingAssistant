from google import genai
import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Read API key from .env
API_KEY = os.getenv("GOOGLE_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def analyze_event_with_gemini(event_name):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=event_name
        )

        # Return AI response
        if response and hasattr(response, "text") and response.text:
            return response.text

        return "No response from AI."

    except Exception as e:
        logging.error(f"Gemini API error: {e}")
        return "AI temporarily unavailable. Please try again later."