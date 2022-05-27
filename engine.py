from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from credentials import *

user_name = PG_USER_NAME
password = PG_PASSWORD
ip_address = IPADDRESS
port = PORT
db_name = DB_NAME

postgres_str = (f'postgresql://{user_name}:{password}@{ip_address}:{port}/{db_name}'.format(user_name=PG_USER_NAME,
                                                                                            password=PG_PASSWORD,
                                                                                            ip_address=IPADDRESS,
                                                                                            port=PORT,
                                                                                        db_name=DB_NAME))
# create an engine
cnx = create_engine(postgres_str)

# create a configured "Session" class
Session = sessionmaker(bind=cnx)

# create a session
session = Session()

# base
Base = declarative_base()

# need to create an auto incrementing
