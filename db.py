from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id=Column(Integer,primary_key=True)
	name=Column(String(100))
	email=Column(String(100))
	des=Column(String(100))
	
class User(Base):
	__tablename__='user'
	id=Column(Integer,primary_key=True)
	email=Column(String(100),nullable=False)
	password=Column(String(20),nullable=False)

engine=create_engine('sqlite:///iiit.db')
Base.metadata.create_all(engine)
print("Database is Created!!!")