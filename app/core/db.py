import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session




load_dotenv() #load the .env credentials and initalize the server

 #read the credentials whit a alias for dont expose the real credentials
DB_HOST = os.getenv("PGHOST")
DB_PORT  = os.getenv("PGPORT")
DB_USER  = os.getenv("PGUSER")
DB_PASSWORD  = os.getenv("PGPASSWORD")
DB_NAME  = os.getenv("PGDATABASE")
sslmode="require"

    
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
)

engine = create_engine(DATABASE_URL,echo = True )

def  get_session():
    with Session(engine) as session:
        yield session

