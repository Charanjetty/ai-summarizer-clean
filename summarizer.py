import vertexai
from vertexai.preview.generative_models import GenerativeModel
from google.oauth2 import service_account
import os

# Load service account securely (local path only!)
SERVICE_ACCOUNT_PATH = "service_account.json"  # don't commit this file

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_PATH
)

# Initialize Vertex AI with credentials
vertexai.init(
    project="ai-powered-document-summarizer",
    location="us-central1",
    credentials=credentials
)

# Load Gemini model
model = GenerativeModel("gemini-2.0-flash-001")

def summarize_text(text: str) -> str:
    """Summarizes input text using Gemini 2.0 Flash."""
    try:
        prompt = f"Summarize the following document:\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating summary: {str(e)}"
