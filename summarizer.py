import json
import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel
from google.oauth2 import service_account

# ✅ Load service account credentials from Streamlit secrets
service_account_info = json.loads(st.secrets["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
credentials = service_account.Credentials.from_service_account_info(service_account_info)

# ✅ Get project info from secrets
project_id = st.secrets["project"]["project_id"]
location = st.secrets["project"]["location"]

# ✅ Initialize Vertex AI client
vertexai.init(project=project_id, location=location, credentials=credentials)

# ✅ Load Gemini model
model = GenerativeModel("gemini-2.0-flash-001")

def summarize_text(text: str) -> str:
    try:
        prompt = f"Summarize the following document:\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating summary: {str(e)}"
