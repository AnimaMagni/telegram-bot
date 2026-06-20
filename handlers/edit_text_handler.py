from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

async def edit_text_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["new_post_text"] = (
        update.message.text
    )

    context.user_data["state"] = (
        "waiting_new_date"
    )

    now = datetime.now().strftime(
    "%Y-%m-%d %H:%M"
)

    await update.message.reply_text(
        f"""
    📅 تاریخ و زمان را وارد کنید

    ⏰ زمان فعلی سیستم:
    {now}

    مثال:
    2026-06-20 20:30
    """
    )