from telegram import Update
from telegram.ext import ContextTypes


async def handle_channel_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    print(update)

    await update.message.reply_text(
        "پیام دریافت شد ✅"
    )