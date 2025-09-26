from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Divya123@localhost/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Divya123@127.0.0.1:3307/todoapplicationdatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})  # for sqlite3
# engine = create_engine(SQLALCHEMY_DATABASE_URL) #for postgresSQL and mysql

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



