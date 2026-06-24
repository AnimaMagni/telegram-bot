from datetime import datetime

from database.models import (
    get_pending_posts,
    mark_post_as_sent
)


async def check_scheduled_posts(context):

    posts = get_pending_posts()

    print(f"Pending Posts: {len(posts)}")

    for post in posts:

        (
            post_id,
            channel_id,
            content_type,
            file_id,
            post_text,
            publish_at
        ) = post

        publish_time = datetime.strptime(
            publish_at,
            "%Y-%m-%d %H:%M"
        )

        print("NOW:", datetime.now())
        print("PUBLISH:", publish_time)

        if datetime.now() < publish_time:
            continue

        try:

            if content_type == "text":

                await context.bot.send_message(
                    chat_id=channel_id,
                    text=post_text
                )

            elif content_type == "photo":

                await context.bot.send_photo(
                    chat_id=channel_id,
                    photo=file_id,
                    caption=post_text
                )

            elif content_type == "video":

                await context.bot.send_video(
                    chat_id=channel_id,
                    video=file_id,
                    caption=post_text
                )

            elif content_type == "document":

                await context.bot.send_document(
                    chat_id=channel_id,
                    document=file_id,
                    caption=post_text
                )

            elif content_type == "audio":

                await context.bot.send_audio(
                    chat_id=channel_id,
                    audio=file_id,
                    caption=post_text
                )

            mark_post_as_sent(post_id)

            print(
                f"Post {post_id} sent successfully"
            )

        except Exception as e:

            print(
                f"Error sending post {post_id}: {e}"
            )

            print("NOW =", datetime.now())
            print("PUBLISH =", publish_time)