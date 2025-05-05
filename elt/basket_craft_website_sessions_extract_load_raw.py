# %%
# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy import text

# %%
# Load environment variables from .env file
# This is necessary to keep sensitive information like passwords out of the codebase
load_dotenv()

# %%
# mySQL database connection 

mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_host = os.environ.get('MYSQL_HOST')
mysql_db = os.environ.get('MYSQL_DB')

# %%
# Postgres Database connection
postgres_user = os.environ.get('POSTGRES_USER')
postgres_password = os.environ.get('POSTGRES_PASSWORD')
postgres_host = os.environ.get('POSTGRES_HOST')
postgres_db = os.environ.get('POSTGRES_DB')
# %%
# Create a connection to the databases
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
mysql_engine = create_engine(mysql_conn_str)
pg_conn_str = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}'
pg_engine = create_engine(pg_conn_str)

# %%
# Get data from MySQL database
df = pd.read_sql("SELECT * FROM website_sessions WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';", mysql_engine)
df
# %%
# Truncate the raw.website_sessions table to clear old data
with pg_engine.connect() as connection:
    connection.execute(text("TRUNCATE TABLE raw.website_sessions CASCADE"))

# Append the new data without dropping the tables 
df.to_sql('website_sessions', pg_engine, schema='raw', if_exists='append', index=False)


# %%
print('Data loaded into Postgres successfully!')