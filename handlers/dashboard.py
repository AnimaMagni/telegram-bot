from telegram import Update
from telegram.ext import ContextTypes

from database.models import (
    count_channels,
    count_scheduled_posts,
    count_sent_posts
)


async def dashboard_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    channels = count_channels(user_id)

    scheduled = count_scheduled_posts(
        user_id
    )

    sent = count_sent_posts(
        user_id
    )

    await update.message.reply_text(
        f"""
📊 داشبورد

📢 کانال‌ها:
{channels}

⏳ پست‌های زمان‌بندی شده:
{scheduled}

✅ پست‌های ارسال شده:
{sent}
"""
    )