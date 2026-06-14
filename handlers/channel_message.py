from telegram import Update
from telegram.ext import ContextTypes
from database.models import save_channel



async def handle_channel_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    
    if update.message.forward_from_chat:

        channel = update.message.forward_from_chat

        save_channel(
            user_id=update.effective_user.id,
            channel_id=channel.id,
            channel_name=channel.title,
            channel_username=channel.username
        )
        await update.message.reply_text(
            f"""
    ✅ کانال متصل شد

    Name: {channel.title}

    Username: @{channel.username}

    ID:
    {channel.id}
    """
        )

    else:

        await update.message.reply_text(
            "❌ لطفاً یک پیام از کانال فوروارد کنید."
            )


    await update.message.reply_text(
        "پیام دریافت شد ✅"
    )