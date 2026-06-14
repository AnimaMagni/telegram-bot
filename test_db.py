import sqlite3

conn = sqlite3.connect("data/bot.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM channels")

rows = cursor.fetchall()

print(rows)

conn.close()