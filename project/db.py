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
    sql = "SELECT * FROM studentscores"
    params = []
    conditions = []
    print("""Please select an option:
    0) filter by id
    1) filter by name
    2) filer by score
    3) filter by status
    4) query entire db 
    """)
    choice = {1,2,3,4,0}
    
    while True :
        try:
            choices = int(input("select a filter"))
            if choices not in choice:
                print("answer out of range please try again")
            else :
                  print(choices)
                  break
        except ValueError :
             print("invalif input\n this field must be a interger (1-5)") 

    if choices == 0:
        while True:
            try:
                id_value = int(input("enter the ID: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        conditions.append("id = %s")
        params.append(id_value)
    elif choices == 1:
        name_value = input("enter the name")
        conditions.append("name = %s")
        params.append(name_value)
    elif choices == 2:
        score_value = int(input("enter the score"))
        conditions.append("score = %s")
        params.append(score_value)
    elif choices == 3 :
        status_values=input("enter the status")
        conditions.append("status = %s")
        params.append(status_values)
    elif choices == 4 :
         pass 
              
            
            
    if conditions:
        sql += " WHERE " + " AND ".join(conditions)
    if params:
        cur.execute(sql,params)
    else:
        cur.execute(sql)




    rows = cur.fetchall()
    print("Listing students...")
 

    print(rows)
    cur.close()
    conn.close()             





