from database.db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS channels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            channel_id INTEGER,
            channel_name TEXT,
            channel_username TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scheduled_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            channel_id INTEGER,
            post_text TEXT,
            publish_at TEXT,
            is_sent INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    

def save_channel(
    user_id,
    channel_id,
    channel_name,
    channel_username
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
            """
            INSERT INTO channels
            (
                user_id,
                channel_id,
                channel_name,
                channel_username
            )
            VALUES (?, ?, ?, ?)
            """,
            (
            user_id,
            channel_id,
            channel_name,
            channel_username
        )
    )
    conn.commit()
    conn.close()

def get_user_channels(user_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            channel_id,
            channel_name,
            channel_username
        FROM channels
        WHERE user_id = ?
        """,
        (user_id,)
    )

    channels = cursor.fetchall()

    conn.close()

    return channels


def channel_exists(user_id, channel_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM channels
        WHERE user_id = ?
        AND channel_id = ?
        """,
        (user_id, channel_id)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None
def save_scheduled_post(
    user_id,
    channel_id,
    post_text,
    publish_at
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scheduled_posts
        (
            user_id,
            channel_id,
            post_text,
            publish_at
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            channel_id,
            post_text,
            publish_at
        )
    )

    conn.commit()
    conn.close()

def get_pending_posts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            channel_id,
            post_text,
            publish_at
        FROM scheduled_posts
        WHERE is_sent = 0
        """
    )

    posts = cursor.fetchall()

    conn.close()

    return posts

def mark_post_as_sent(post_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE scheduled_posts
        SET is_sent = 1
        WHERE id = ?
        """,
        (post_id,)
    )

    conn.commit()
    conn.close()


def get_user_scheduled_posts(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sp.id,
            c.channel_name,
            sp.post_text,
            sp.publish_at
        FROM scheduled_posts sp
        JOIN channels c
        ON sp.channel_id = c.channel_id
        WHERE sp.user_id = ?
        AND sp.is_sent = 0
        ORDER BY sp.publish_at
        """,
        (user_id,)
    )

    posts = cursor.fetchall()

    conn.close()

    return posts


def get_scheduled_post(post_id, user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sp.id,
            c.channel_name,
            sp.post_text,
            sp.publish_at
        FROM scheduled_posts sp
        JOIN channels c
        ON sp.channel_id = c.channel_id
        WHERE sp.id = ?
        AND sp.user_id = ?
        AND sp.is_sent = 0
        """,
        (post_id, user_id)
    )

    post = cursor.fetchone()

    conn.close()

    return post


def delete_scheduled_post(post_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM scheduled_posts
        WHERE id = ?
        """,
        (post_id,)
    )

    conn.commit()
    conn.close()
    
