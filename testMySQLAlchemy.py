from sqlalchemy import MetaData, create_engine, select, Table, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase,sessionmaker, relationship
from sqlalchemy import create_engine




host, port, userName, password= 'localhost', 3306, 'root', '01234567'
engine= create_engine(f"mysql+pymysql://{userName}:{password}@{host}:{port}/testdb")


class Base(DeclarativeBase):
    pass
class TestBook(Base):
    __tablename__= 'testbook'
    id= Column(Integer, primary_key=True, autoincrement=True)
    title= Column(String(100), nullable=False)
    author= Column(String(40), nullable=False)
    date= Column(Date)


Session = sessionmaker(bind=engine)
session = Session()
def createTable():
    Base.metadata.create_all(engine)


# createTable()


# 新增資料
def insert(data):
    session.add(data)
    session.commit()
# insert(TestBook(title="C###", author="GOD"))


# 讀取資料
ret= session.query(TestBook).all()
for i in ret:
    print(i.title, i.author, i.date, sep='\t')


