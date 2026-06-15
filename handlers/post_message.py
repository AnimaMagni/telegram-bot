from database.models import get_user_channels
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def post_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    state = context.user_data.get("state")

    if state != "waiting_post":
        return

    post_text = update.message.text

    context.user_data["post_text"] = post_text
    context.user_data["state"] = "waiting_channel"

    user_id = update.effective_user.id
    channels = get_user_channels(user_id)

    if not channels:
        await update.message.reply_text("❌ هنوز کانالی نداری.")
        return

    keyboard = [[channel[1]] for channel in channels]  # اسم کانال‌ها

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        "📢 حالا کانال را انتخاب کنید:",
        reply_markup=reply_markup
    )