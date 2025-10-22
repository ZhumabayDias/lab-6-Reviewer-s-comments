import sqlite3

def init_db(path="users.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
    cur.execute("DELETE FROM users")
    cur.executemany("INSERT INTO users (username, password) VALUES (?, ?)", [
        ("alice", "alice_pass"),
        ("bob", "bob_pass"),
        ("admin", "supersecret"),
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("DB initialized (users.db)")