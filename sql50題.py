from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, PrimaryKeyConstraint, select, func
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import pandas as pd

host, port, userName, password= 'localhost', 3306, 'root', '01234567'
engine= create_engine(f"mysql+pymysql://{userName}:{password}@{host}:{port}/testdb")


# 方法一
meta= MetaData()
student= Table('student', meta,
    Column('sno', String(10), primary_key=True),
    Column('sname', String(20)),
    Column('sage', Integer()),
    Column('ssex', String(5))
)
teacher= Table('teacher', meta,
    Column('tno', String(10), primary_key=True),
    Column('tname', String(20))
)
course= Table('course', meta,
    Column('cno', String(10)),
    Column('cname', String(10)),
    Column('tno', String(10)),
    PrimaryKeyConstraint('tno','cno', name='pk_course')
)
sc= Table('sc', meta,
    Column('sno', String(10)),
    Column('cno', String(10)),
    Column('score', Float(4,2)),
    PrimaryKeyConstraint('sno','cno', name='pk_sc')
)
# meta.create_all(engine)


# 方法二
Base= declarative_base()
class Student(Base):
    __tablename__= 'student'
    sno= Column(String(10), primary_key=True)
    sname= Column(String(20))
    sage= Column(Integer())
    ssex= Column(String(5))
class Teacher(Base):
    __tablename__= 'teacher'
    tno= Column(String(10), primary_key=True)
    tname= Column(String(20))
class Course(Base):
    __tablename__= 'course'
    cno= Column(String(10))
    cname= Column(String(10))
    tno= Column(String(10))
    __table_args__ = (PrimaryKeyConstraint('tno','cno', name='pk_course'),)
class Sc(Base):
    __tablename__= 'sc'
    sno= Column(String(10))
    cno= Column(String(10))
    score= Column(Float(4,2))
    __table_args__ = (PrimaryKeyConstraint('sno','cno', name='pk_sc'),)
Base.metadata.create_all(engine)


session= sessionmaker(bind=engine)()
def exc(cmd):
    with engine.connect() as conn:
        result= pd.DataFrame(conn.execute(cmd))
        print(result)
        return result


# r= exc(select(Student))
# print(r[:10], len(r[:10]))
exc(select(Sc.__table__.columns).where(Sc.score > 60))



# --------------------------------------------------------------------------------------

dataInput= {'studentData': '''
insert into student values ('s001','張三',23,'男');
insert into student values ('s002','李四',23,'男');
insert into student values ('s003','吳鵬',25,'男');
insert into student values ('s004','琴沁',20,'女');
insert into student values ('s005','王麗',20,'女');
insert into student values ('s006','李波',21,'男');
insert into student values ('s007','劉玉',21,'男');
insert into student values ('s008','蕭蓉',21,'女');
insert into student values ('s009','陳蕭曉',23,'女');
insert into student values ('s010','陳美',22,'女');
insert into student values ('s011','王麗',24,'女');
insert into student values ('s012','蕭蓉',20,'女');
''',
'teacherData': '''
insert into teacher values ('t001', '劉陽');
insert into teacher values ('t002', '諶燕');
insert into teacher values ('t003', '胡明星');
''',
'courseData': '''
insert into course values ('c001','J2SE','t002');
insert into course values ('c002','Java Web','t002');
insert into course values ('c003','SSH','t001');
insert into course values ('c004','Oracle','t001');
insert into course values ('c005','SQL SERVER 2005','t003');
insert into course values ('c006','C#','t003');
insert into course values ('c007','JavaScript','t002');
insert into course values ('c008','DIV+CSS','t001');
insert into course values ('c009','PHP','t003');
insert into course values ('c010','EJB3.0','t002');
''',
'scData': '''
insert into sc values ('s001','c001',78.9);
insert into sc values ('s002','c001',80.9);
insert into sc values ('s003','c001',81.9);
insert into sc values ('s004','c001',50.9);
insert into sc values ('s005','c001',59.9);
insert into sc values ('s001','c002',82.9);
insert into sc values ('s002','c002',72.9);
insert into sc values ('s003','c002',82.9);
insert into sc values ('s001','c003',59);
insert into sc values ('s006','c003',99.8);
insert into sc values ('s002','c004',52.9);
insert into sc values ('s003','c004',20.9);
insert into sc values ('s004','c004',59.8);
insert into sc values ('s005','c004',50.8);
insert into sc values ('s002','c005',92.9);
insert into sc values ('s001','c007',78.9);
insert into sc values ('s001','c010',78.9);
'''}

import pymysql
def dbC(command):
    conn= pymysql.connect(host= "localhost", port= 3306, user= "root", passwd= "01234567", charset= "utf8", db= "testdb")
    with conn.cursor() as cursor:
        cursor.execute(command)
        data= cursor.fetchall()
        conn.commit()
    conn.close()
    return data
# for commonds in dataInput.values():
#     for commond in commonds.split('\n'):
#         if commond.strip():
#             dbC(commond)

