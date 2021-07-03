# 创建表中的字段(列)
from sqlalchemy import Column
# 表中字段的属性
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker

from utils.connect_db import Base, engine


class Lucky_draw_activity(Base):

    __tablename__ = 'lucky_draw_activity'

    id = Column(Integer, primary_key=True)
    winner_uid = Column(Integer)
    winner_number = Column(Integer)
    created_time = Column(String(100))
    updated_time = Column(String(100))

    def __repr__(self):
        return "<Lucky_draw_activity(id='{}', winner_uid='{}', winner_number='{}', created_time='{}', updated_time='{}')>".format(
            self.id, self.winner_uid, self.winner_number, self.created_time, self.updated_time)


if __name__ == "__main__":
    import time
    # step 4: 建立表
    # Base.metadata.create_all(engine)

    # step 5: 声明会话类, 方式一声明并绑定engine
    Session = sessionmaker(bind=engine)

    # step 6: 实例化会话类
    session = Session()

    # step 7: 操作数据库
    result = engine.execute("show tables;")
    print(result.fetchall())

    ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    config_data = Lucky_draw_activity(id='1',
                     winner_uid='111', created_time=ctime, updated_time=None)

    session.add(config_data)

    session.commit()

    result = engine.execute("select * from test_td.lucky_draw_activity;")
    print(result.fetchall())