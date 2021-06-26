# 创建表中的字段(列)
from sqlalchemy import Column
# 表中字段的属性
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker

from utils.connect_db import Base, engine


class Lucky_draw_employee(Base):

    __tablename__ = 'lucky_draw_employee'

    uid = Column(Integer, primary_key=True)
    uname = Column(String(100))
    status = Column(String(100))

    def __repr__(self):
        return "<Lucky_draw_employee(uid='{}', uname='{}', status='{}')>".format(
            self.uid, self.uname, self.status)


if __name__ == "__main__":

    # step 5: 声明会话类, 方式一声明并绑定engine
    Session = sessionmaker(bind=engine)

    # step 6: 实例化会话类
    session = Session()

    # step 7: 操作数据库
    employee_data = Lucky_draw_employee(uid='8', uname='aj', status='在职')

    session.add(employee_data)

    session.commit()

    result = engine.execute("select * from test_td.lucky_draw_employee;")
    print(result.fetchall())

    print(employee_data.__repr__())