from sqlalchemy.orm import sessionmaker
from p11_sqlalchemy.orm_create import Teacher, engine

# 插入数据

# yg_teacher为映射类的实例，实例对象只是在此刻环境的内存中有效，并没有在表中真正生成数据
yg_teacher1 = Teacher(name='amity1',
               age='18',
               city='sh')

yg_teacher2 = Teacher(name='amity1',
               age='19',
               city='bj')

# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)

# 创建会话的实例session
session = Session()

# 通过实例插入数据
session.add(yg_teacher1)
session.add(yg_teacher2)

# 查询实例中name为amity的数据
our_teacher = session.query(Teacher).filter_by(
    name='amity1').first()
our_teacher_sql = session.query(Teacher).filter_by(
    name='amity1')
print("Find which name is amity: ", our_teacher, our_teacher_sql, "\n\n")


# 提交，数据真正的被写入到数据库中了
session.commit()