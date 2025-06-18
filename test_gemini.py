print("Script started...")

import vertexai
from vertexai.preview.generative_models import GenerativeModel

try:
    vertexai.init(project="ai-powered-document-summarizer", location="us-central1")
    print("Vertex AI initialized.")

    model = GenerativeModel("gemini-2.0-flash-001")
    print("Model loaded.")

    response = model.generate_content("Summarize: Python is a programming language.")
    print("Generated Summary:")
    print(response.text)
except Exception as e:
    print("Error occurred:", e)
