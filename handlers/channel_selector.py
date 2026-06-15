from telegram import Update
from telegram.ext import ContextTypes

from database.models import get_user_channels


async def channel_selector(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get("state")

    print("CHANNEL SELECTOR RUNNING")
    print("MESSAGE =", update.message.text)

    if state != "waiting_channel":
        return

    selected_channel = update.message.text

    channels = get_user_channels(
        update.effective_user.id
    )

    for channel in channels:

        channel_id, name, username = channel

        if name == selected_channel:

            print("Selected:", selected_channel)
            print("Channels:", channels)
            print(
                "Post Text:",
                context.user_data.get("post_text")
            )
            print("Channel ID:", channel_id)

            context.user_data[
                "selected_channel_id"
            ] = channel_id

            context.user_data[
                "state"
            ] = "waiting_date"

            await update.message.reply_text(
                f"📢 کانال {name} انتخاب شد."
            )

            await update.message.reply_text(
                "📅 تاریخ و زمان را وارد کنید.\n\n"
                "مثال:\n"
                "2026-06-20 20:30"
            )

            return

    await update.message.reply_text(
        "❌ کانال انتخاب شده پیدا نشد."
    )