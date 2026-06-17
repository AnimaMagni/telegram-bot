from telegram import Update
from telegram.ext import ContextTypes
from database.models import (
    save_scheduled_post
)
from datetime import datetime



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
    save_scheduled_post(
    user_id=update.effective_user.id,
    channel_id=context.user_data[
        "selected_channel_id"
    ],
    post_text=context.user_data[
        "post_text"
    ],
    publish_at=publish_at
    )

    await update.message.reply_text(
        f"""
    ✅ پست زمان‌بندی شد

    📝 متن:
    {context.user_data["post_text"]}

    ⏰ زمان:
    {publish_at}
    """
    )
    context.user_data.clear()

    publish_time = datetime.strptime(
    publish_at,
    "%Y-%m-%d %H:%M"
)

    if publish_time <= datetime.now():

        await update.message.reply_text(
            "❌ زمان وارد شده گذشته است."
        )

        return