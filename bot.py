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
TOKEN = "8998358080:Here is the token for bot GoldWaechter_123_bot @GoldWaechter_David_bot:

8998358080:AAF-NpC7oFHAQvlNwhAEpnXfr1UNFnb4V5M

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot läuft erfolgreich in der Cloud...")
    await application.run_polling()

if __name__ == '__main__':
    keep_alive() # Startet den Webserver-Trick
    asyncio.run(main()) # Startet den Bot
    

