from telegram import Update
from telegram.ext import ContextTypes
from database.models import save_channel
from database.models import (
    save_channel,
    channel_exists
)




async def handle_channel_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    state = context.user_data.get("state")

    #  حالت انتخاب کانال بعد از post
    if state == "waiting_channel":
        selected_channel_name = update.message.text

        context.user_data["selected_channel"] = selected_channel_name

        context.user_data["state"] = None

        await update.message.reply_text(
            f"✅ کانال انتخاب شد: {selected_channel_name}\n"
            f"📤 پست آماده ارسال است."
        )

        return

    #  حالت قبلی (فوروارد کانال)
    if update.message.forward_from_chat:

        channel = update.message.forward_from_chat

        if channel_exists(user_id, channel.id):

            await update.message.reply_text(
                "⚠️ این کانال قبلاً متصل شده است."
            )
            return
        

        try:

            bot_member = await context.bot.get_chat_member(
                chat_id=channel.id,
                user_id=context.bot.id
            )

        except Exception:

            await update.message.reply_text(
                "❌ ربات در این کانال عضو نیست.\n\nابتدا ربات را به کانال اضافه کنید."
            )

            return
    


        if bot_member.status not in [
            "administrator",
            "creator"
        ]:

            await update.message.reply_text(
                "❌ ربات ادمین این کانال نیست.\n\nلطفاً ربات را Administrator کنید."
            )

            return

        save_channel(
            user_id=user_id,
            channel_id=channel.id,
            channel_name=channel.title,
            channel_username=channel.username
        )

        await update.message.reply_text(
            f"""
✅ کانال متصل شد

Name: {channel.title}
Username: @{channel.username}
ID: {channel.id}
"""
        )

    else:
        await update.message.reply_text(
            "❌ لطفاً یک پیام از کانال فوروارد کنید."
        )


#    await update.message.reply_text(
 #       "پیام دریافت شد ✅"
  #  )


    print(bot_member.status)

    