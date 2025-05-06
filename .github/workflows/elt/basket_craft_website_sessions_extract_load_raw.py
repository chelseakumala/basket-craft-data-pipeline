!pip install PyMySQL


import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

# Verify the credentials are correct for the MySQL database
mysql_engine = create_engine(
    "mysql+pymysql://analyst:isba_7415@db.isba.co/basket_craft" # Make sure username, password, host, and database name are correct.
)

pg_engine = create_engine(
    "postgresql+psycopg2://admin:isba_4715@your_pg_host:5432/your_pg_db"
)

query = """
SELECT *
FROM website_sessions
WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';
"""

try:
    df = pd.read_sql(query, mysql_engine)
    print("Data fetched successfully!")
except sqlalchemy.exc.OperationalError as e:
    print(f"Error connecting to the database: {e}")
    print("Please verify your credentials, user privileges, and network connectivity.")
   
