# utils/summarizer.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def summarize_news(news_text):
    """
    Generate a concise summary of a news article using Groq LLM.

    Args:
        news_text (str): Full news article text

    Returns:
        str: AI-generated summary
    """

    # Check if API key exists
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY not found."

    # Groq API endpoint
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Prompt sent to the LLM
    prompt = f"""
You are a professional news analyst.

Summarize the following news article in 5 concise bullet points.

News Article:
{news_text}
"""

    # API headers
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Request payload
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }

    try:
        # Send POST request
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        # Convert response to JSON
        result = response.json()

        # Debug: print API response in terminal
        print(result)

        # Check if API returned an error
        if "choices" not in result:
            return f"Groq API Error: {result}"

        # Extract summary
        summary = result["choices"][0]["message"]["content"]

        return summary

    except Exception as e:
        return f"Error generating summary: {str(e)}"
