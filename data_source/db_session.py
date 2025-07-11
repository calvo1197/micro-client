from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .configuration import Config

# prepare_connection
engine = create_engine(Config.SQL_ALCHEMY_DATABASE_URI)

# create orm session
orm_session = sessionmaker(bind = engine)