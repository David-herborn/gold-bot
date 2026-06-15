import logging
from telegram.ext import ApplicationBuilder
import asyncio

# Hier deinen Telegram-Token einfügen
TOKEN = "DEIN_TOKEN_HIER"

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot läuft erfolgreich in der Cloud...")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
