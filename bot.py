import logging
from telegram.ext import ApplicationBuilder
import asyncio
from flask import Flask
from threading import Thread
import os

# --- Webserver-Trick für Render ---
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# --- Dein eigentlicher Bot ---
TOKEN = "8998358080:AAEuF7AUlMzHkZbmQHowslAZPxV54hi4l5I# Hier deinen echten Token einfügen

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot läuft erfolgreich in der Cloud...")
    await application.run_polling()

if __name__ == '__main__':
    keep_alive() # Startet den Webserver-Trick
    asyncio.run(main()) # Startet den Bot
