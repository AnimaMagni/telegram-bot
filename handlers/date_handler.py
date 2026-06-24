from telegram import Update
from telegram.ext import ContextTypes
from database.models import save_scheduled_post
from datetime import datetime


async def date_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get("state")

    if state != "waiting_date":
        return

    publish_at = update.message.text

    try:

        publish_time = datetime.strptime(
            publish_at,
            "%Y-%m-%d %H:%M"
        )

    except ValueError:

        await update.message.reply_text(
            "❌ فرمت تاریخ اشتباه است.\n\nمثال:\n2026-06-20 20:30"
        )

        return

    if publish_time <= datetime.now():

        await update.message.reply_text(
            "❌ زمان وارد شده گذشته است."
        )

        return

    post_id = save_scheduled_post(
        user_id=update.effective_user.id,
        channel_id=context.user_data[
            "selected_channel_id"
        ],
        content_type=context.user_data[
            "content_type"
        ],
        file_id=context.user_data[
            "file_id"
        ],
        post_text=context.user_data[
            "post_text"
        ],
        publish_at=publish_at
    )

    await update.message.reply_text(
        f"""
✅ پست زمان‌بندی شد

🆔 ID:
{post_id}

📝 متن:
{context.user_data["post_text"]}

⏰ زمان:
{publish_at}
"""
    )

    context.user_data.clear()