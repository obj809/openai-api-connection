# How to Guide: OpenAI API Connection

## Description

A Python quickstart guide for getting started with the OpenAI API.

## Requirements
- Python 3.10+
- An OpenAI API key

## main.py

```python

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY not set")

MODEL = "gpt-5-nano"

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model=MODEL,
    input="Write a one-sentence bedtime story about a dragon who is afraid of the dark."
)

print(response.output_text)
```

## Build Steps


1) Create an OpenAI account
[https://openai.com/api/](https://openai.com/api/)


2) Create an OpenAI API key
Once logged in:
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)


3) Clone this repo
```bash
git clone https://github.com/obj809/openai-api-connection
```
```bash
cd openai-api-connection
```


4) Create a virtual environment
```bash
python -m venv venv
```


5) Activate the virtual environment
macOS / Linux
```bash
source venv/bin/activate
```
Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```


6) Install requirements
```bash
pip install -r requirements.txt
```

Minimum dependencies:
```bash
pip install openai python-dotenv
```


7) Create a .env file in the project root

OPENAI_API_KEY=your_api_key_here


8) Run main.py
```bash
python main.py
```


## Links

- [OpenAI API Models](https://platform.openai.com/docs/models)

- [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart?language=python)