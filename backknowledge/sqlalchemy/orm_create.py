from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# step 1: 创建engine
# 创建一个实例引擎,它代表了一个数据库的核心接口
engine = create_engine(
    "mysql+pymysql://root:12345678@127.0.0.1:3306/test?charset=utf8mb4",
    echo=True,
    max_overflow=5)

# step 2: 创建Session方法，由于step6的操作没有用到具体的表，故省去此步骤

# step 3: Model中定义的表继承Base
Base = declarative_base()
# 将我们Engine作为数据库连接源传递，使用MetaData 为所有数据库中尚不存在的表向数据库发出CREATE TABLE语句。
# 即teacher这个表在base的metadata里，但是在库里不存在，执行此语句会创建teacher表
Base.metadata.create_all(engine)

# step 4: 定义表
class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(12))
    age = Column(String(2))
    city = Column(String(16))

    def __repr__(self):
        tpl = "Teacher(id={}, name={}, age={}, city={})"
        return tpl.format(self.id, self.name,
                          self.age, self.city)



# step 5: 创建session会话实例对象，由于step6的操作没有用到具体的表，故省去此步骤

# step 6: 操作数据库
result = engine.execute("show tables;")
print(result.fetchall())
