
# 基础配置 config： create_lucky_draw, set_serial_scope, set_biggest_serial_winning_odds

def create_lucky_draw():
    # lucky_draw_activity
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

