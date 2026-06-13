from telegram import Update
from telegram.ext import ContextTypes


async def connect_channel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "📢 یک پیام از کانال خود را برای من فوروارد کنید."
    )