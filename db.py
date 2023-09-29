import sqlite3


def insert_member(user_id, first_name, last_name, username):
    con = sqlite3.connect("algobot.db")
    cur = con.cursor()
    sql = f"INSERT OR REPLACE INTO members (user_id, first_name, last_name, username) VALUES ({user_id},'{first_name}', '{last_name}', '{username}')"
    cur.execute(sql)
    con.commit()
    con.close()


def select_members():
    con = sqlite3.connect("algobot.db")
    cur = con.cursor()
    sql = f"SELECT user_id FROM members"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    con.close()
    return data
