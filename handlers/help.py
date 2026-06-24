from telegram import Update
from telegram.ext import ContextTypes

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        """
📌 دستورات ربات:

/start - شروع ربات
/help - نمایش راهنما
/post   زمان‌بندی و انتشار خودکار
/dashboard - مشاهده آمار و اطلاعات کانال‌ها
/channels مدیریت کانال های شما
🚀 قابلیت‌های آینده:
*درست کردن پلی لیست براساس نام خواننده برای موزیک چنل ها 
"""
    )