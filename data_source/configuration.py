import os
from .secrets import get_secret

#get data environment vars 
name_db = os.getenv("NAME_DB")
user_db=get_secret("db-user")
password_db=get_secret("db-password")
ip_db = os.getenv("IP_DB")
port_db = os.getenv("PORT_DB")

class Config:
    SQL_ALCHEMY_DATABASE_URI = f"mysql+pymysql://{user_db}:{password_db}@{ip_db}:{port_db}/{name_db}"
    SQL_ALCHEMY_TRACK_MODIFICATION = False
