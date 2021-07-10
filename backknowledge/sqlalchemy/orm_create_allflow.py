from sqlalchemy import Table, MetaData
from sqlalchemy.orm import mapper

# 创建连接相关
from sqlalchemy import create_engine

# 和 sqlapi 交互，执行转换后的 sql 语句，用于创建基类
from sqlalchemy.ext.declarative import declarative_base

# 创建表中的字段(列)
from sqlalchemy import Column

# 表中字段的属性
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

# step 1: 创建engine，创建连接对象，并使用 pymsql 引擎
'''
1）通过create_engine()建立连接，create_engine是 Engine实例，create_engine第一次调用的时候会调用Engine.execute()或者 Engine.connect()方法，
    通过dialect在数据库和DBAPI之间建立连接关系。
    注意：返回create_engine对象并没有连接到数据库。只有在执行第一次要求对数据库时才连接
    2）echo是SQLAlchemy logging 是个标准logging模型。当echo 为True看到所有生成的SQL；希望少输出,设置它 False
    3）mysql+pymysql://admin:admin@192.168.6.22/coursesys?charset=utf8 是个dialect连接
    4）engine=create_engine('sqlite:///:memory:',echo=True)将使用一个只在内存中SQLite数据库
'''
conn_str = "mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}?charset=utf8mb4"
connect_info = conn_str.format(user='htc',
                               pwd='123456',
                               host='10.16.2.5',
                               db_name='test_td')
engine = create_engine(connect_info, echo=True, max_overflow=5)

# step 2: 创建表定义中继承的基类
# 我们使用ORM：映射类与数据库表。SQLAlchemy在中首先通过declarative_base申明一个基类，这个基类维持着类与数据库表的关系，即声明映射
Base = declarative_base()

# step 3: 定义表，或叫声明表，方式一
'''声明表第一种方式：在自定义类继承declarative_base这个基类来映射数据表
    __tablename__指定表名
　　 Column 指定字段
　　 primary_key 设置主键
　　 __repr__ 当打印User对象时显示的数据。
'''
class Person(Base):

    __tablename__ = 'person'  # 表名

    id = Column(Integer, primary_key=True)
    # 在oracleo等数据库中，有可能需要用到序列，你可以通过Sequence来使用
    # id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # 必须指定长度，在PostgreSQL上不需要
    name = Column(String(32))
    age = Column(Integer)  # 整型

    def __repr__(self):
        return "<Person(id='{}', name='{}', age='{}')>".format(
            self.id, self.name, self.age)

    __table_args__ = (
        # 设置联合唯一
        UniqueConstraint('id', 'name', name='uix_id_name'),

        # 建立索引
        # Index('uix_id_name', 'name'),
    )

# step 3: 定义表，或叫声明表，方式二
metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User, user)
'''
User.__table__打印的结果如下：
Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, prima
ry_key=True, nullable=False), Column('name', String(), table=<users>), Column('f
ullname', String(), table=<users>), schema=None)


'''
# step 4: 建立表
'''
向数据库发出建表，完成类与表的映射，在数据库中生成所有继承declarative_base表

MetaData是一个注册表包括能够一组执行的命令到数据库，上面声明了表的类，但是数据库中并没有创建表，
通过Base.metadata.create_all(engine)向数据库发出建表完成类与表的映射

如果数据库里该表存在则不需要建表，不存在才建；
推荐先在数据库里建好表，而非自动创建表
'''
Base.metadata.create_all(engine)


# step 5: 声明会话类, 方式一声明并绑定engine
Session = sessionmaker(bind=engine)
''' 方式二：
如果还没有engine,先创建engine，在通过configure绑定到session
Session = sessionmaker()
Session.configure(bind=engine)
'''

# step 6: 实例化会话类
session = Session()


# step 7: 操作数据库
result = engine.execute("show tables;")
print(result.fetchall())
# 7.1: 增加数据
ed_person=Person(id=1, name="ed", age=18)
session.add(ed_person)
session.commit()
# 7.2: 获取id
print(ed_person.id)
# 7.3: 查询数据
our_person = session.query(Person).filter_by(name='ed').first()
print(our_person)
# 7.4: 修改数据 1
ed_person.name = '11111'
ed_person.age = 99
our_person.age = 100
# 修改数据 2  update的参数只接受传json, 返回是否更新成功
result = session.query(Person).filter_by(id=1).update({"age":19})
print("The updated record is: ", result)
session.commit()
print("------------")

# 7.5: 查看脏数据
print(session.dirty)
# 7.6: 增加一组数据
result = session.add_all([User(name='wendy', fullname='Wendy Williams', password='111111'), User(name='mary', fullname='Mary Contrary', password='111111'), User(name='fred', fullname='Fred Flinstone', password='111111')])
print("7.6: ", result)
#表示查看新增加的数据
print(session.new)
'''
IdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
<User(name='fred', fullname='Fred Flinstone', password='blah')>])
'''
# 7.8: 删除数据
session.delete(ed_person)
# 7.9: 排序后查询第一条记录的字段id
user_id = session.query(User).order_by(User.id).first().id # 默认升序
user_id = session.query(User).order_by(User.id.desc()).first().id # 降序
from sqlalchemy import desc
user_id = session.query(User).order_by(desc('id')).first().id # 降序

# 7.10: 提交数据回滚数据
# 上面的数据并没有在数据库中，需要通过commit()方法把数据提交到数据库中，获取通过rollback回滚数据。
session.rollback()
session.commit()


# 其他
def init_db():
    """创建所有定义的表到数据库中"""
    Base.metadata.create_all(engine)

def drop_db():
    """从数据库中删除所有定义的表"""
    Base.metadata.drop_all(engine)

# 执行创建表
init_db()


