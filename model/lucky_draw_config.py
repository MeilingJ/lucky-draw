# 创建表中的字段(列)
from sqlalchemy import Column, ForeignKey
# 表中字段的属性
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker

from utils.connect_db import Base, engine


class Lucky_draw_config(Base):

    __tablename__ = 'lucky_draw_config'  # 表名

    lucky_draw_activity_id = Column(Integer, ForeignKey('lucky_draw_activity.id'))
    type = Column(String(100))
    serial_scope = Column(Integer)
    biggest_serial_winning_odds = Column(Integer)

    def __repr__(self):
        return "<Lucky_draw_config(lucky_draw_activity_id='{}', type='{}', serial_scope='{}', biggest_serial_winning_odds='{}')>".format(
            self.lucky_draw_activity_id, self.type, self.serial_scope, self.biggest_serial_winning_odds)


if __name__ == "__main__":
    # step 4: 建立表
    # Base.metadata.create_all(engine)

    # step 5: 声明会话类, 方式一声明并绑定engine
    Session = sessionmaker(bind=engine)

    # step 6: 实例化会话类
    session = Session()

    # step 7: 操作数据库
    result = engine.execute("show tables;")
    print(result.fetchall())

    config_data = Lucky_draw_config(lucky_draw_activity_id='4',
                     type='CUSTOM', serial_scope=10000, biggest_serial_winning_odds=99)

    session.add(config_data)

    session.commit()

    result = engine.execute("select * from test_td.lucky_draw_config;")
    print(result.fetchall())