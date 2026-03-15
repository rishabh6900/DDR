import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# load environment variables
load_dotenv()

def configure_gemini():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in the .env file.")

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=api_key,   # <-- important
        temperature=0.2
    )

    return model