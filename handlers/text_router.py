from handlers.menu_handler import (
    menu_handler
)
from handlers.post_message import (
    post_message_handler
)

from handlers.channel_selector import (
    channel_selector
)

from handlers.date_handler import (
    date_handler
)
from handlers.cancel_handler import (
    cancel_handler
)
from handlers.edit_id_handler import (
    edit_id_handler
)
from handlers.edit_text_handler import (
    edit_text_handler
)
from handlers.edit_date_handler import (
    edit_date_handler
)




async def text_router(
    update,
    context
):

    text = update.message.text

    if text in [
        "📝 پست جدید",
        "📅 پست‌های زمان‌بندی شده",
        "📊 داشبورد",
        "📢 کانال‌های من",
        "❓ راهنما"
    ]:

        await menu_handler(
            update,
            context
        )

        return

    state = context.user_data.get(
        "state"
    )

    if state == "waiting_post":

        await post_message_handler(
            update,
            context
        )

    elif state == "waiting_channel":

        await channel_selector(
            update,
            context
        )

    elif state == "waiting_date":

        await date_handler(
            update,
            context
        )

    elif state == "waiting_cancel_id":

        await cancel_handler(
            update,
            context
        )

    elif state == "waiting_edit_id":

        await edit_id_handler(
            update,
            context
        )

    elif state == "waiting_new_text":

        await edit_text_handler(
            update,
            context
        )

    elif state == "waiting_new_date":

        await edit_date_handler(
            update,
            context
        )