from telegram import Update
from telegram.ext import ContextTypes


async def edit_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["state"] = "waiting_edit_id"

    await update.message.reply_text(
        "🆔 شناسه پست را وارد کنید."
    )