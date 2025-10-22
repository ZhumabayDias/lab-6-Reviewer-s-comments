# good_query.py
import sqlite3
import sys

DB = "users.db"

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def find_user_by_id_safe(user_input):
   # Validation: expecting an integer
    if not is_int(user_input):
        raise ValueError("Invalid id format: must be integer")
    user_id = int(user_input)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Parameterized query (secure)
    cur.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 good_query.py <id>")
        print("Example safe id: 1")
        sys.exit(1)
    inp = sys.argv[1]
    try:
        res = find_user_by_id_safe(inp)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    if not res:
        print("No rows")
    else:
        for r in res:
            print(r)