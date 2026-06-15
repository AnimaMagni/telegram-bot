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
