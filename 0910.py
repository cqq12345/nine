import  datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

lianjie= create_engine( 'mysql+pymysql://cqq:123.@localhost:3306/xx')
Base=declarative_base(bind=lianjie)
Session=sessionmaker(bind=lianjie)

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(20), unique=True)
    birthday=Column(Date)
    money=Column(Float,default= 0.0)

Base.metadata.create_all()

bob = User(name='bob', birthday=datetime.date(1990, 3, 21), money=234)
tom = User(name='tom', birthday=datetime.date(1995, 9, 12), money=444)
lucy = User(name='lucy', birthday=datetime.date(1998, 5, 14), money=300)
jam = User(name='jam', birthday=datetime.date(1994, 3, 9), money=58)
alex = User(name='alex', birthday=datetime.date(1992, 3, 17), money=99)
eva = User(name='eva', birthday=datetime.date(1987, 7, 28), money=175)
rob = User(name='rob', birthday=datetime.date(1974, 2, 5), money=274)
session =Session()

session.add_all([bob,tom,lucy])
session.commit()

