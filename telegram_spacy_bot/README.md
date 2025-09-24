Telegram spaCy Chatbot: Entity and POS Assistant

Problem this solves
Many chat interactions benefit from quick natural-language insights: named entities (people, places, dates) and parts of speech (nouns, verbs). This bot enables fast text inspection right inside Telegram for students and analysts who want to understand or debug language data.

What the bot does
- Responds to any text message by extracting named entities and token part-of-speech tags using spaCy
- Offers simple commands: /start, /help, /model
- Gracefully handles unexpected input with a friendly fallback message

Limitations
- The small English model (en_core_web_sm) may miss entities or mislabel tokens
- Very long messages or non-English text may yield poor results
- If spaCy model is missing or env variables are not set, the bot will not start; the error message explains how to fix it
- On errors during analysis, the bot replies with a generic apology and suggests trying simpler text

Prerequisites
- Python 3.10+
- Telegram bot token from BotFather

Setup (recommended with a virtual environment)
Windows PowerShell:
1) Create and activate venv in project folder
   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2) Install requirements
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

3) Set environment variables for the session
   $env:TELEGRAM_TOKEN = "<your-bot-token>"
   $env:SPACY_MODEL = "en_core_web_sm"

4) Run the bot
   python bot.py

Verification steps
- In Telegram, search for your bot and start a chat
- Send: Johannesburg is sunny on 2025-09-24.
- Expected: Entities include Johannesburg (GPE) and 2025-09-24 (DATE); tokens are listed with POS tags

Project files
- bot.py: Telegram bot using python-telegram-bot v20+ and spaCy
- requirements.txt: Dependencies for recreating the environment
- .gitignore: Excludes venv and local env files

Security note
Do not commit your TELEGRAM_TOKEN to version control. Use environment variables or a .env file that is excluded.


