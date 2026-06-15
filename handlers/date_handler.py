from telegram import Update
from telegram.ext import ContextTypes


async def date_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get(
        "state"
    )

    if state != "waiting_date":
        return

    publish_at = update.message.text

    await update.message.reply_text(
        f"✅ زمان دریافت شد:\n{publish_at}"
    )