from telegram import Update
from telegram.ext import ContextTypes


async def post_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["state"] = "waiting_post"

    await update.message.reply_text(
        "📝 متن پست را ارسال کنید."
    )