from telegram import Update
from telegram.ext import ContextTypes

from database.models import get_user_channels


async def channels_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    channels = get_user_channels(user_id)

    if not channels:

        await update.message.reply_text(
            "❌ هنوز کانالی متصل نکرده‌ای."
        )

        return

    text = "📋 کانال‌های متصل شده\n\n"

    for index, channel in enumerate(channels, start=1):

        channel_id, name, username = channel

        text += (
            f"{index}. {name}\n"
            f"@{username}\n\n"
        )

    await update.message.reply_text(text)