from database.models import get_user_channels
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes


async def post_message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    state = context.user_data.get("state")

    if state != "waiting_post":
        return

    # متن
    if update.message.text:

        context.user_data["content_type"] = "text"
        context.user_data["file_id"] = None
        context.user_data["post_text"] = (
            update.message.text
        )

    # عکس
    elif update.message.photo:

        context.user_data["content_type"] = "photo"
        context.user_data["file_id"] = (
            update.message.photo[-1].file_id
        )

        context.user_data["post_text"] = (
            update.message.caption or ""
        )

    # ویدیو
    elif update.message.video:

        context.user_data["content_type"] = "video"
        context.user_data["file_id"] = (
            update.message.video.file_id
        )

        context.user_data["post_text"] = (
            update.message.caption or ""
        )

    # فایل
    elif update.message.document:

        context.user_data["content_type"] = "document"
        context.user_data["file_id"] = (
            update.message.document.file_id
        )

        context.user_data["post_text"] = (
            update.message.caption or ""
        )

    # آهنگ
    elif update.message.audio:

        context.user_data["content_type"] = "audio"
        context.user_data["file_id"] = (
            update.message.audio.file_id
        )

        context.user_data["post_text"] = (
            update.message.caption or ""
        )

    else:

        await update.message.reply_text(
            "❌ فعلاً متن، عکس، ویدیو، فایل و آهنگ پشتیبانی می‌شوند."
        )

        return

    context.user_data["state"] = "waiting_channel"

    user_id = update.effective_user.id
    channels = get_user_channels(user_id)

    if not channels:

        await update.message.reply_text(
            "❌ هنوز کانالی نداری."
        )

        return

    keyboard = [
        [channel[1]]
        for channel in channels
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        "📢 حالا کانال را انتخاب کنید:",
        reply_markup=reply_markup
    )

    print("POST HANDLER RUNNING")
    print("TYPE =", context.user_data["content_type"])