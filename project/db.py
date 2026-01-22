import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #load the .env credentials and initalize the server
def get_connection():
    
    return psycopg2.connect(
        host = os.getenv("PGHOST"),
        port = os.getenv("PGPORT"),
        user = os.getenv("PGUSER"),
        password = os.getenv("PGPASSWORD"),
        dbname = os.getenv("PGDATABASE"),
        sslmode = "require"
 )
    #read the credentials whit a alias for dont expose the real credentials

def list_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM studentscores")
    rows = cur.fetchall()
    print("Listing students...")
    print(rows)
    cur.close()
    conn.close()





