from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)
from bot.config import BOT_TOKEN
from handlers.start import start
from handlers.help import help_command
from handlers.connect import connect_channel
from handlers.channels import channels_command
from handlers.post import post_command

from handlers.channel_message import (
    handle_channel_message
)
from handlers.text_router import (
    text_router
)
from handlers.error_handler import (
    error_handler
)
from services.scheduler import (
    check_scheduled_posts
)
from handlers.scheduled import (
    scheduled_command
)
from handlers.cancel import (
    cancel_command
)







def create_app():

    app = Application.builder().token(
        BOT_TOKEN
    ).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        CommandHandler(
            "connect",
            connect_channel
        )
    )

    app.add_handler(
        CommandHandler(
            "channels",
            channels_command
        )
    )

    app.add_handler(
    CommandHandler(
        "scheduled",
        scheduled_command
        )
    )


    app.add_handler(
        CommandHandler(
            "post",
            post_command
        )
    )
    app.add_handler(
    CommandHandler(
        "cancel",
        cancel_command
        )
    )
    

    app.add_handler(
        MessageHandler(
            filters.FORWARDED,
            handle_channel_message
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_router
        )
    )

    app.add_error_handler(
        error_handler
    )

    app.job_queue.run_repeating(
    check_scheduled_posts,
    interval=30,
    first=10
    )
    return app