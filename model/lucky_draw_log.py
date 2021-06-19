# 创建表中的字段(列)
from sqlalchemy import Column
# 表中字段的属性
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import sessionmaker

from utils.connect_db import Base, engine


class Lucky_draw_log(Base):

    __tablename__ = 'lucky_draw_log'

    id = Column(Integer, primary_key=True)
    lucky_draw_activity_id = Column(Integer)
    uid = Column(Integer)
    serial_code = Column(Integer)
    winning_odds = Column(Float)
    created_time = Column(String(100))

    def __repr__(self):
        return "<lucky_draw_log(id='{}', lucky_draw_activity_id='{}', uid='{}', serial_code='{}', winning_odds='{}', created_time='{}')>".format(
            self.id, self.lucky_draw_activity_id, self.uid, self.serial_code, self.winning_odds, self.created_time)


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

    config_data = Lucky_draw_log(id='1', lucky_draw_activity_id='111', uid=1, serial_code=333, winning_odds=0.8, created_time=ctime)

    session.add(config_data)

    session.commit()

    result = engine.execute("select * from test_td.lucky_draw_log;")
    print(result.fetchall())