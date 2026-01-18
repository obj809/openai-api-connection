# main.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY not set")

MODEL = "gpt-5-nano"
PROMPT = "Write a one-sentence bedtime story about a dragon who is afraid of the dark."

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model=MODEL,
    input=PROMPT
)

print(response.output_text)