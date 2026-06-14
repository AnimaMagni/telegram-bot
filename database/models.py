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

