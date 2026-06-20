from telegram import Update
from telegram.ext import ContextTypes


async def connect_channel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        """
📢 اتصال کانال

قبل از اتصال کانال، مراحل زیر را انجام دهید:

1️⃣ ربات را به کانال خود اضافه کنید.

2️⃣ ربات را Administrator کنید.

3️⃣ مجوز ارسال پیام را فعال کنید.

4️⃣ یک پیام از همان کانال برای ربات فوروارد کنید.

پس از دریافت پیام، کانال به حساب شما متصل خواهد شد.
"""
    )