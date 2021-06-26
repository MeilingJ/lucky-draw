from model.lucky_draw_activity import Lucky_draw_activity
from utils.connect_db import session
from utils.utils import current_time
# 基础配置 config： create_lucky_draw, set_serial_scope, set_biggest_serial_winning_odds


def create_lucky_draw():
    '''
    在lucky_draw_activity表里创建一条记录
    :return: id
    '''
    ld_activity = Lucky_draw_activity(created_time=current_time)
    session.add(ld_activity)
    session.commit()

def set_lucky_draw_config(scope, odds):
    # 在lucky_draw_config表里创建一条记录
    pass


def set_serial_scope(self, scope):
    '''
    设置序列号取值范围
    :return:
    '''
    self.serial_scope = scope


def set_biggest_serial_winning_odds(self, odds):
    '''
    设置最大序列号中奖概率
    入参，最大取值；
    :return:
    '''
    self.biggest_serial_winning_odds = odds


if __name__ == "__main__":
    create_lucky_draw()