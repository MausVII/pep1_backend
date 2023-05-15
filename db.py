import mysql.connector
from sqlalchemy import create_engine
from db_config import user, password, host, port, database

def get_connection():
    return create_engine(F"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")