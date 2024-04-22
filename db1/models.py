from sqlalchemy.sql.sqltypes import Integer, String
from db1.database import Base
from sqlalchemy import  Column

class Db1User(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    email = Column(String)
    password =Column(String)