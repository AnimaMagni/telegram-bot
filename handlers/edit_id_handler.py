from telegram import Update
from telegram.ext import ContextTypes

from database.models import get_post_by_id


async def edit_id_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    post_id = update.message.text

    if not post_id.isdigit():

        await update.message.reply_text(
            "❌ شناسه نامعتبر است."
        )

        return

    post = get_post_by_id(
        int(post_id),
        update.effective_user.id
    )

    if not post:

        await update.message.reply_text(
            "❌ چنین پستی پیدا نشد."
        )

        return

    _, post_text, publish_at = post

    context.user_data["edit_post_id"] = int(post_id)
    context.user_data["state"] = "waiting_new_text"

    await update.message.reply_text(
        f"""
📝 متن فعلی:

{post_text}

⏰ زمان فعلی:
{publish_at}

متن جدید را ارسال کنید.
"""
    )