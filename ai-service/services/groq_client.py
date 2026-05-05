import requests
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def load_prompt(user_input):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, "..", "prompts", "analyze_prompt.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
            template = f.read()

        return template.replace("{user_input}", user_input)

    except Exception as e:
        logging.error(f"Prompt load error: {e}")
        return user_input  # fallback


def call_groq(user_input):
    if not API_KEY:
        logging.error("Missing GROQ_API_KEY")
        return None

    prompt = load_prompt(user_input)
    retries = 3

    for attempt in range(retries):
        try:
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }

            response = requests.post(
                URL,
                headers=HEADERS,
                json=data,
                timeout=10   
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            else:
                logging.warning(f"Groq API error: {response.status_code} - {response.text}")

        except requests.exceptions.Timeout:
            logging.warning("Request timeout")

        except Exception as e:
            logging.error(f"Exception: {e}")

        # exponential backoff
        time.sleep(2 ** attempt)

    logging.error("Groq failed after retries")
    return None