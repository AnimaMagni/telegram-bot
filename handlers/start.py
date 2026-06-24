from telegram import (
    Update,
    ReplyKeyboardMarkup
)
from telegram.ext import ContextTypes


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        ["📝 پست جدید"],
        ["📅 پست‌های زمان‌بندی شده"],
        ["📊 داشبورد"],
        ["📢 کانال‌های من"],
        ["❓ راهنما"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        """
🤖 Telegram Scheduler Bot

به پنل مدیریت خوش آمدید.
""",
        reply_markup=reply_markup
    )