# 创建连接相关
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 和 sqlapi 交互，执行转换后的 sql 语句，用于创建基类
from sqlalchemy.ext.declarative import declarative_base

# step 1: 创建engine，创建连接对象，并使用 pymsql 引擎
conn_str = "mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}?charset=utf8mb4"
connect_info = conn_str.format(user='htc',
                               pwd='123456',
                               host='10.16.2.5',
                               db_name='test_td')
engine = create_engine(connect_info, echo=True, max_overflow=5)

# step 2: 创建表定义中继承的基类
# 我们使用ORM：映射类与数据库表。SQLAlchemy在中首先通过declarative_base申明一个基类，这个基类维持着类与数据库表的关系，即声明映射
Base = declarative_base()

# step 5: 声明会话类, 方式一声明并绑定engine
Session = sessionmaker(bind=engine)

# step 6: 实例化会话类
session = Session()

