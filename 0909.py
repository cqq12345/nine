
import  datetime
from sqlalchemy import create_engine# 连接引擎
from sqlalchemy.orm import sessionmaker#持续连接，创建会话
from sqlalchemy import Column, String, Integer, Float, Date
#Column（列） String（） Integer（） Float（） Date（）
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://cqq:123.@localhost:3306/qq")  # seamile:5422(用户名与密码)xiongda（数据库）
Base = declarative_base(bind=engine)  # 创建模型的基础类
Session = sessionmaker(bind=engine)  # 创建会话类


class User(Base):  # （类本身对应数据库里的表结构）
    '''User 模型'''
    __tablename__ = 'user'  # 该模型对应的表名
    id = Column(Integer, primary_key=True)  # 定义 id 字段
    name = Column(String(20), unique=True)  # 定义姓名字段
    birthday = Column(Date)  # 定
    money = Column(Float, default=0.0)  # 定义城市
    # 字段


Base.metadata.create_all()  # 创建表结构


# 定义⼀些对象，对应数据库里的一行

bob = User(name='bob', birthday=datetime.date(1990, 3, 21), money=234)
tom = User(name='tom', birthday=datetime.date(1995, 9, 12), money=444)
lucy = User(name='lucy', birthday=datetime.date(1998, 5, 14), money=300)
jam = User(name='jam', birthday=datetime.date(1994, 3, 9), money=58)
alex = User(name='alex', birthday=datetime.date(1992, 3, 17), money=99)
eva = User(name='eva', birthday=datetime.date(1987, 7, 28), money=175)
rob = User(name='rob', birthday=datetime.date(1974, 2, 5), money=274)
ella = User(name='ella', birthday=datetime.date(1999, 5, 26), money=394)
# 增加数据
session = Session()#（定义与数据库的会话，都是通过这个操作）
session.add_all([bob, tom, lucy, jam])  # 在 Session 中记录操
session.commit()  # 提交到数据库中执⾏

# 删除数据
session.delete(jam)  # 记录删除操作（只能删除一个数据）
session.commit()  # 提交到数据库中执⾏

# 修改数据
tom.money = 270  # 修改数据 ，想改什么就写什么，只能用name删
session.commit()  # 提交到数据库中执⾏

# 查询数据
u_query = session.query(User)
user = u_query.filter_by(id=1).one()#（这种比较好）
print(user.name)
users = u_query.filter(User.id > 2).order_by('birthday')#（filter: 需要指明用户）
for u in users:
    print(u.name, u.birthday, u.money)

# 根据查询结果进⾏更新
users(user.id == 1).update({'ciyt:beijing'}, synchronize_session=False)
users.update({'money': User.money - 1}, synchronize_session=False)
session.commit()

# 按数量取出数据: limit / offset
users = u_query.limit(3).offset(4)
for u in users:
    print(u.id, u.name)
