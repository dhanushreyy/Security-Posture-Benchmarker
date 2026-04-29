import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def load_prompt(user_input):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_dir, "..", "prompts", "analyze_prompt.txt")

    with open(prompt_path, "r") as f:
        template = f.read()

    return template.replace("{user_input}", user_input)


def call_groq(user_input):
    prompt = load_prompt(user_input)  # use structured prompt
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

            response = requests.post(URL, headers=HEADERS, json=data)

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            else:
                print(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Exception: {e}")

        # exponential backoff
        time.sleep(2 ** attempt)

    return "Failed after retries"