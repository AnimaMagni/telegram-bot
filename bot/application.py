from telegram.ext import Application, CommandHandler
from handlers.help import help_command
from handlers.error_handler import error_handler
from bot.config import BOT_TOKEN
from handlers.start import start
from handlers.connect import connect_channel

from telegram.ext import MessageHandler, filters
from handlers.channel_message import (
    handle_channel_message
)



def create_app():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
    CommandHandler("connect", connect_channel)
    )
    app.add_handler(
    MessageHandler(
        filters.ALL,
        handle_channel_message
    )
    )
    app.add_error_handler(error_handler)
    return app