from telegram import Update
from telegram.ext import ContextTypes

from handlers.post import post_command
from handlers.channels import channels_command
from handlers.scheduled import scheduled_command
from handlers.dashboard import dashboard_command
from handlers.help import help_command


async def menu_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "📝 پست جدید":

        await post_command(
            update,
            context
        )

    elif text == "📢 کانال‌های من":

        await channels_command(
            update,
            context
        )

    elif text == "📅 پست‌های زمان‌بندی شده":

        await scheduled_command(
            update,
            context
        )

    elif text == "📊 داشبورد":

        await dashboard_command(
            update,
            context
        )

    elif text == "❓ راهنما":

        await help_command(
            update,
            context
        )