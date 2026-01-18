import os , psycopg2  # import os and psy for psql 
from dotenv import load_dotenv #for read the .env archive and dont expose de credentials

load_dotenv() #load the .env credentials and initalize the server
conn = None
try :
    conn = psycopg2.connect(   #read the credentials whit a alias for dont expose the real credentials
    host = os.getenv("PGHOST"),
    port = os.getenv("PGPORT"),
    user = os.getenv("PGUSER"),
    password = os.getenv("PGPASSWORD"),
    dbname = os.getenv("PGDATABASE"), 
    sslmode="require"
)
    print("connection status : properly connected")
except psycopg2.OperationalError:
    print("internal server error : code error 500")
finally :
    if conn is not  None:
        conn.close


