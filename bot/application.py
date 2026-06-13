from telegram.ext import Application, CommandHandler

from bot.config import BOT_TOKEN
from handlers.start import start


def create_app():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    return app