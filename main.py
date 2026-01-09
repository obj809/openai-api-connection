# main.py

from dotenv import load_dotenv
import os
from openai import OpenAI
from prompts import prompt

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY not set")

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

print(response.output_text)