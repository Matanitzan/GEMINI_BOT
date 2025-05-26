import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key was loaded correctly
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in the .env file.")

# Define the Gemini Flash model endpoint
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# User message (prompt)
prompt_text = "מה שלומך היום?"

# Construct the request payload
data = {
    "contents": [
        {
            "parts": [
                {"text": prompt_text}
            ]
        }
    ]
}

# Send the POST request with API key
response = requests.post(
    url=f"{API_URL}?key={api_key}",
    headers={"Content-Type": "application/json"},
    json=data
)

# Handle and display the response
if response.status_code == 200:
    # Extract and print the full response from Gemini
    reply = response.json()
    output_text = reply['candidates'][0]['content']['parts'][0]['text']
    print("Gemini response:")
    print(output_text)
else:
    print("Error occurred:")
    print(f"Status code: {response.status_code}")
    print(response.text)
