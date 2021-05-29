from sqlalchemy.orm import sessionmaker
from p11_sqlalchemy.orm_create import Teacher, engine

# 更新数据

# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)

# 创建会话的实例session
session = Session()

# 新增数据
session.add(Teacher(name='shark2',
                    age='18',
                    city='ZhengZhou'))

# 修改已有数据的字段值,只是发生于会话对象的事务中，并没有发生在数据库中。
shark=session.query(Teacher).filter_by(name='shark2').first()
print("shark----------------", shark)
print("shark.age------------", shark.age)
shark.age = '28'
shark.name = 'shark3'

# 查询操作结果
query_result = session.query(Teacher).filter(Teacher.name.in_(['shark2','shark3'])).all()
print("query_result-------------", query_result)

session.rollback()

query_result = session.query(Teacher).filter(Teacher.name.in_(['shark2','shark3'])).all()
print("query_result-------------", query_result)

session.commit()