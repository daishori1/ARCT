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
        while True:
            try:
                score_value = int(input("enter the score"))
                break
            except ValueError:
                print("invalid input ,please enter a number ")
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



def add_student():
    conn = get_connection()
    cur = conn.cursor()
    params = []
    query = "INSERT INTO studentscores (name , score , status) values (%s , %s , %s )"

    name_value = input("give the name of the student")
    params.append(name_value)
    while True:
        try:
            score_value = int(input("give me the score of the student"))
            break
        except ValueError:
            print("this field must be a number")
    params.append(score_value)
    if score_value >= 90 :
        status_value = "Excellence"
        params.append(status_value)
    elif score_value >= 70  :
        status_value = "aproved"
        params.append(status_value)
    elif score_value >= 30:
        status_value = "failed"
        params.append(status_value)
    else :
        status_value = "repeat"
        params.append(status_value)
    
    try:
        cur.execute(query, params)
        conn.commit()
        print("Student added!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()


def update_score():
    conn = get_connection()
    cur = conn.cursor()
    params = []
    query = "UPDATE studentscores SET score = %s, status = %s WHERE id = %s"
    
    # 1. Pedir ID del estudiante (con validación while/try)
    # 2. Pedir nuevo score (con validación while/try)
    # 3. Calcular nuevo status según el score (copiar lógica de add_student)
    # 4. Construir params = [nuevo_score, nuevo_status, id_estudiante]
    # 5. Pedir confirmación
    # 6. Si no confirma: return
    # 7. execute y commit
    # 8. Verificar rowcount
    # 9. close




def delete_student():
    conn = get_connection()
    cur = conn.cursor()
    params = []
    query = " DELETE FROM studentscores " 
    print("""Please select an option:
    0) delete by id
    1) delete by name 
    """)
    choice = {0,1}
    while True:
        try:
            choises = int(input("select a option for delete by "))
            if choises not in choice:
                print("answer out of range please try again")
            else :
               print(choice)
               break
        except ValueError:
            print("please put a valid int (0-1)")
    if choises == 0 :
        while True:
            try:
                id_value = int(input("enter the id to delete"))
                break
            except ValueError:
                print("invalid input this field must be a interger")
        query += " WHERE id = %s "
        params.append(id_value)
    elif choises == 1 :
        name_value = input("enter the name to delete")
        query += " WHERE name = %s "
        params.append(name_value)

    confirm = input(f"Are you sure you want to delete? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Deletion cancelled")
        cur.close()
        conn.close()
    
        return

    cur.execute(query, params)
    conn.commit()


    if cur.rowcount > 0:
        print(f"{cur.rowcount} student(s) deleted")
    else:
        print("No student found with that criteria")

    cur.close()
    conn.close()
