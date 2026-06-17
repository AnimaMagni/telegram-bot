from telegram import Update
from telegram.ext import ContextTypes

from database.models import (
    get_scheduled_post,
    delete_scheduled_post
)


async def cancel_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get("state")

    if state != "waiting_cancel_id":
        return

    try:

        post_id = int(update.message.text)

    except ValueError:

        await update.message.reply_text(
            "❌ شناسه معتبر نیست."
        )

        return

    post = get_scheduled_post(
        post_id,
        update.effective_user.id
    )

    if not post:

        await update.message.reply_text(
            "❌ پست پیدا نشد."
        )

        return

    _, post_text = post

    delete_scheduled_post(post_id)

    await update.message.reply_text(
        f"""
❌ پست زمان‌بندی شده حذف شد.

📝 متن:

{post_text}
"""
    )

    context.user_data.clear()