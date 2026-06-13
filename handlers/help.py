from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    1 / 0
    await update.message.reply_text(
        """
📌 دستورات ربات:

/start - شروع ربات
/help - نمایش راهنما

🚀 قابلیت‌های آینده:

• زمان‌بندی پست
• انتشار خودکار
• آمار بازدید
• آمار ری‌اکشن‌ها
"""
    )