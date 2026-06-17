from telegram import Update
from telegram.ext import ContextTypes

from database.models import (
    get_user_scheduled_posts
)


async def scheduled_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    posts = get_user_scheduled_posts(
        update.effective_user.id
    )

    if not posts:

        await update.message.reply_text(
            "📭 هیچ پست زمان‌بندی شده‌ای ندارید."
        )

        return

    text = "📅 پست‌های زمان‌بندی شده\n\n"

    for post in posts:

        post_id, channel_name, post_text, publish_at = post

        text += (
            f"🆔 {post_id}\n"
            f"📢 {channel_name}\n"
            f"⏰ {publish_at}\n"
            f"📝 {post_text[:40]}\n\n"
        )

    await update.message.reply_text(text)