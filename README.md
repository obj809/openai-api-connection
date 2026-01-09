# How to Guide: OpenAI API Connection

## Description

A Python quickstart guide for getting started with the OpenAI API.

## Requirements
- Python 3.10+

## main.py

```python


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
```

## Build Steps


1) Create an OpenAI account
[https://openai.com/api/](https://openai.com/api/)


2) Create an API key 
Once logged in:
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)


3) Clone this repo
```bash
git clone https://github.com/obj809/openai-api-connection
```
```bash
cd openai-api-connection
```


4) Create venv
```bash
python -m venv venv
```


5) Activate venv
macOS / Linux
```bash
source venv/bin/activate
```
Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```


5) Install requirements.txt 
```bash
pip install -r requirements.txt
```


6. (Optional) Edit the prompt value in prompts.py


7) Run main.py
```bash
python main.py
```


# Links

[https://platform.openai.com/docs/quickstart?language=python](https://platform.openai.com/docs/quickstart?language=python)