#firts test to get the data from the DB
from db import get_connection

def list_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM studentscores")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows 


print(list_students())

