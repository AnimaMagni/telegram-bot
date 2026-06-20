from telegram import Update
from telegram.ext import ContextTypes

from database.models import (
    update_scheduled_post
)


async def edit_date_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    post_id = context.user_data[
        "edit_post_id"
    ]

    new_text = context.user_data[
        "new_post_text"
    ]

    new_date = update.message.text

    update_scheduled_post(
        post_id=post_id,
        post_text=new_text,
        publish_at=new_date
    )

    await update.message.reply_text(
        f"""
✅ پست ویرایش شد

🆔 {post_id}

📝 متن جدید:
{new_text}

⏰ زمان جدید:
{new_date}
"""
    )

    context.user_data.clear()