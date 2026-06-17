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



async def text_router(
    update,
    context
):

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