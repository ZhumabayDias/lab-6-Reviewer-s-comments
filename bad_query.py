import sqlite3
import sys

DB = "users.db"

def find_user_by_id(user_input):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # DANGER: Direct inclusion of user input in an SQL query
    query = "SELECT id, username FROM users WHERE id = " + user_input
    print("Executing query:", query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bad_query.py <id>")
        print("Example safe id: 1")
        print("Example attack payload: 1 OR 1=1")
        sys.exit(1)
    inp = sys.argv[1]
    try:
        res = find_user_by_id(inp)
    except Exception as e:
        print("Error executing query:", e)
        sys.exit(1)
    if not res:
        print("No rows")
    else:
        for r in res:
            print(r)