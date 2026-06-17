from telegram import Update
from telegram.ext import ContextTypes


async def cancel_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["state"] = "waiting_cancel_id"

    await update.message.reply_text(
        "🆔 شناسه پست را ارسال کنید."
    )