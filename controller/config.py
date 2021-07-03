from model.lucky_draw_activity import Lucky_draw_activity
from model.lucky_draw_config import Lucky_draw_config
from utils.connect_db import session
from utils.utils import current_time
# 基础配置 config： create_lucky_draw, set_serial_scope, set_biggest_serial_winning_odds


def create_lucky_draw_activity():
    '''
    在lucky_draw_activity表里创建一条记录
    :return: id
    '''
    ld_activity = Lucky_draw_activity(created_time=current_time)
    session.add(ld_activity)
    session.commit()
    id = session.query(Lucky_draw_activity).order_by(Lucky_draw_activity.id.desc()).first().id
    return id

def set_lucky_draw_config(ld_id, scope, odds):
    # 在lucky_draw_config表里创建一条记录

    ld_config = Lucky_draw_config(lucky_draw_activity_id=ld_id, type='CUSTOM', serial_scope=scope, biggest_serial_winning_odds=odds)
    session.add(ld_config)
    session.commit()


if __name__ == "__main__":
    id = create_lucky_draw_activity()
    set_lucky_draw_config(id, 10000, 90)