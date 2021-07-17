import random
import time

from model.lucky_draw_employee import Lucky_draw_employee
from model.lucky_draw_log import Lucky_draw_log
from model.lucky_draw_activity import Lucky_draw_activity
from model.lucky_draw_config import Lucky_draw_config
from utils.connect_db import session


def get_employees():
    employees = session.query(Lucky_draw_employee.uid).all()
    print("参与人的员工id：", employees)
    return employees


def generate_random_serial(employees, serial_scope):
    """
    随机生成序列号
    # 入参，员工列表 employees
    # 出参，员工序列号分配结果employees_serial [序列号,序列号,...]
    :return:
    """

    employees_serial = []
    for i in range(len(employees)):
        employees_serial.append(round(random.random() * serial_scope))
    print("随机生成员工的序列号：", employees_serial)
    return employees_serial


def calculate_winning_odds(employees_serial, biggest_serial_winning_odds):
    """
    计算中奖概率
    入参，员工序列号分配结果employees_serial, [271, 271, 271, 2888, ...]
    出参，员工序列号对应的中奖概率结果employees_winning_odds
    :return: max_odds, other_odds
    """
    employees_winning_odds = []
    max_num = 0
    max_odds = None
    other_odds = None

    employees_num = len(employees_serial)
    max_serial = max(employees_serial)
    print("最大序列号为：", max_serial)
    print("最大序列号type为：", type(max_serial))

    for i in range(employees_num):
        if employees_serial[i] == max_serial:
            max_num = max_num + 1

    print("获得最大序列号的人数：", max_num)

    if max_num == employees_num:
        other_odds = 0
        max_odds = 1/max_num
    else:
        max_odds = biggest_serial_winning_odds / max_num
        other_odds = (1 - biggest_serial_winning_odds) / (employees_num - max_num)

    print("获得最大序列号的人的中奖概率", max_odds)
    print("获得非最大序列号的人的中奖概率：", other_odds)

    for i in range(employees_num):
        if employees_serial[i] == max_serial:
            employees_winning_odds.append(max_odds)
        else:
            employees_winning_odds.append(other_odds)

    return employees_winning_odds


def save_lucky_draw_log(activity_id, employees, employees_serial, employees_winning_odds):
    """
    保存每次抽奖的记录
    :return:
    """

    for i in range(len(employees)):
        log_data = Lucky_draw_log(lucky_draw_activity_id=activity_id, uid=employees[i][0],
                                  serial_code=employees_serial[i], winning_odds=employees_winning_odds[i],
                                  created_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        session.add(log_data)

    session.commit()


def get_employees_no_list(employees, serial_scope, employees_winning_odds):
    """
    生成一个长度为serial_scope的数组，根据某员工的中奖概率计算得到该数组中给到该员工的位置个数，并根据位置个数依次排列员工号
    :return:
    """
    tag_no = 0
    employees_no_list = []
    for i in range(len(employees)):
        nos = round(serial_scope * employees_winning_odds[i])

        if i == 0:
            print("tag: ", nos)
            for j in range(nos):
                employees_no_list.append(employees[i][0])
            tag_no = nos
            print("tag_no: ", tag_no)
        else:
            for j in range(nos):
                employees_no_list.append(employees[i][0])
            tag_no = tag_no + nos
            print("tag_no: ", tag_no)

    return employees_no_list


def save_lucky_draw_activity(activity_id, uid, no):
    """
    保存每次抽奖活动的结果，即中奖人和中奖号
    :return:
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    session.query(Lucky_draw_activity).filter_by(id=activity_id).update({"winner_uid": uid,"winner_number": no,"updated_time":current_time})
    session.commit()


def get_winner(activity_id):
    """
    :param activity_id: 抽奖活动id
    :return: winner_uid
    """
    # 查询参加抽奖的员工
    employees = get_employees()

    # 读抽奖活动配置
    serial_scope = 10000
    biggest_serial_winning_odds = 0.8

    config_data = session.query(Lucky_draw_config).filter_by(lucky_draw_activity_id=activity_id).first()
    print("config_data is: ", config_data)

    if config_data:
        serial_scope = config_data.serial_scope
        biggest_serial_winning_odds = config_data.biggest_serial_winning_odds

    print("Config serial_scope is: ", serial_scope)
    print("Config biggest_serial_winning_odds is: ", biggest_serial_winning_odds)

    # 分配序列号
    employees_serial = generate_random_serial(employees, serial_scope)
    # max_serial = max(employees_serial) # 放在此行不报错

    # 计算中奖概率
    employees_winning_odds = calculate_winning_odds(employees_serial, biggest_serial_winning_odds)
    # max_serial = max(employees_serial) # 放在此行报错

    # 记录中奖概率
    save_lucky_draw_log(activity_id, employees, employees_serial, employees_winning_odds)

    # 生成被抽员工排位
    employees_no_list = get_employees_no_list(employees, serial_scope, employees_winning_odds)
    print("员工排位: ", employees_no_list)

    # 在[0, serial_scope]范围内生成一个随机数
    win_no = round(random.random() * serial_scope)
    print("win_no is:", win_no)

    # 判断随机数作为排位所对应的winner，即员工id
    winner_uid = employees_no_list[win_no]
    print("The winner employees no is: ", winner_uid)

    # 保存每次抽奖活动的结果，即中奖人和中奖号
    save_lucky_draw_activity(activity_id, winner_uid, win_no)

    return winner_uid


if __name__ == "__main__":
    get_winner(1)
