import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s" % user_id
    cur.execute(query)
    return cur.fetchone()