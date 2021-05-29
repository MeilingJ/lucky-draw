import random

class LuckyDraw:

    employees = [] # 员工列表 [(员工号, 员工名),(员工号, 员工名),...]
    # winner = None # 中奖人
    serial_scope = 1000 # 序列号取值范围
    biggest_serial_winning_odds = 0.8 # 最大序列号中奖概率
    employees_winning_odds = None # 员工中奖概率结果，[(员工号, 员工名, 序列号,中奖概率),(员工号, 员工名, 序列号,中奖概率),...]

    def __init__(self, *args):
        '''
        TODO 初始化的时候员工编号唯一性校验
        :param args: 初始化的员工列表
        '''
        if args:
            self.employees = args[0]

    def add_employee(self, employee):
        '''
        TODO 添加员工时校验员工号是否存在
        :param employee: (员工号，员工姓名)
        :return:
        '''
        self.employees.append(employee)

    def delete_employee(self, employee):
        # 1 检查该员工号是否在员工列表中存在set_serial_scope
        # 1.1 如果存在,则校验姓名是否一致，如果一致则删除，如果不一致则报错"该员工号存在，但员工姓名跟系统里的员工姓名不一致，请检查并重新操作！"
        # 1.2 如果不存在, 则报错"该员工号不存在，请检查并重新操作！"
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("The employee is not in the luckydraw system!")

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

    def set_random_serial(self):
        '''
        随机生成序列号
        # 入参，员工列表 employees
        # 出参，员工序列号分配结果employees_serial [序列号,序列号,...]
        :return:
        '''

        employees_serial = []
        for i in range(len(self.employees)):
            employees_serial.append(round(random.random()*self.serial_scope))
        print(employees_serial)
        return employees_serial

    def calculate_winning_odds(self, employees_serial):
        '''
        计算中奖概率
        入参，员工序列号分配结果employees_serial, [271, 271, 271, 2888, ...]
        出参，员工序列号分配结果employees_winning_odds，含中奖概率[(员工号, 员工名, 序列号,中奖概率),(员工号, 员工名, 序列号,中奖概率),...]
        :return:
        '''
        self.employees_winning_odds = []
        max_serial = None
        max_num = 0
        max_odds = None
        other_odds = None

        # 待删掉
        # employees_serial = [271, 271, 271, 2888]
        employees_num = len(employees_serial)
        max_serial = max(employees_serial)
        print(max_serial)

        for i in range(employees_num):
            if employees_serial[i] == max_serial:
                max_num = max_num + 1

        print("获得最大序列号的人数：", max_num)

        if max_num == employees_num:
            other_odds = 0
            max_odds = 1/max_num
        elif max_num == 1:
            max_odds = self.biggest_serial_winning_odds
            other_odds = (1 - self.biggest_serial_winning_odds) / (employees_num - max_num)
        else:
            max_odds = self.biggest_serial_winning_odds / max_num
            other_odds = (1 - self.biggest_serial_winning_odds) / (employees_num - max_num)

        print("获得最大序列号的人的中奖概率", max_odds)
        print("获得非最大序列号的人的中奖概率：", other_odds)

        self.employees_winning_odds = []
        for i in range(employees_num):
            employee_winning_odds = [self.employees[i][0]]
            employee_winning_odds.append(self.employees[i][1])
            employee_winning_odds.append(employees_serial[i])
            if employees_serial[i] == max_serial:
                employee_winning_odds.append(max_odds)
            else:
                employee_winning_odds.append(other_odds)
            self.employees_winning_odds.append(employee_winning_odds)
        print(self.employees_winning_odds)
        return self.employees_winning_odds

    def get_random_no(self, draw_no_socpe):
        win_no = round(random.random()*draw_no_socpe)
        return win_no

    def run_lucky_draw(self):
        '''
        抽奖
        step 1: 随机生成序列号set_random_serial()
        step 2: 计算中奖概率
        step 3: 按概率输出中奖人
        :return:
        '''

        # Step 1：生成序列号
        employees_serial = ldraw.set_random_serial()

        # Step 2：计算中奖概率
        ldraw.calculate_winning_odds(employees_serial)

        # Step 3: 根据人数确定取数范围，TODO 序列号范围serial_scope是否也可根据这个来定？如获取人数，是10的n次方，那么抽奖数据范围是10的n+1次方
        draw_no_socpe = self.serial_scope

        # Step 4: 将概率换算成员工号待抽列表
        '''
        如下问题如何解决？提升计算数值的精准度
        self.employees_winning_odds = [[1, 'jerry', 3205, 0.06666666666666665], [2, 'amity', 9476, 0.8], [3, 'nigel', 1573, 0.06666666666666665], [4, 'girl', 4405, 0.06666666666666665]]
        101 = [7, 80, 7, 7]

        self.employees_winning_odds = [[1, 'jerry', 271, 0.3], [2, 'amity', 271, 0.3], [3, 'nigel', 271, 0.4], [3, 'nigel', 271, 0]]
        100 = [30, 30, 40, 0]
        '''

        tag_no = 0
        employees_no_list = []
        for i in range(len(self.employees)):
            if i == 0:
                nos = round(draw_no_socpe * self.employees_winning_odds[i][3])
                print("tag: ", nos)
                for j in range(nos):
                    employees_no_list.append(self.employees_winning_odds[i][0])
                tag_no = nos
                print("tag_no: ", tag_no)
            else:
                nos = round(draw_no_socpe * self.employees_winning_odds[i][3])
                for j in range(nos):
                    employees_no_list.append(self.employees_winning_odds[i][0])
                tag_no = tag_no + nos
                print("tag_no: ", tag_no)

        print(tag_no)
        print(employees_no_list)

        # Step 5: 生成一个随机数[0, draw_no_socpe]
        win_no = self.get_random_no(draw_no_socpe)
        print("win_no is:", win_no)

        # Step 6: 判断随机数对应的winner

        winner = employees_no_list[win_no]
        print("winner employees no is: ", winner)

        for i in range(len(self.employees)):
            if self.employees[i][0] == winner:
                return self.employees[i]

if __name__ == '__main__':

    # Step 1：录入可以参加抽奖的人
    ldraw = LuckyDraw([(1,'jerry'), (2, 'amity'), (3, 'nigel'), (4, 'cuicui'), (5, 'mengmeng'), (6, 'lily'), (7, 'elf')])
    print("参加抽奖的人有：", ldraw.employees)

    # Step 2：相关设置 -- 可省，用默认值
    ldraw.set_serial_scope(10000)
    ldraw.set_biggest_serial_winning_odds(0.8)

    # Step 5：根据中奖概率抽奖
    winner = ldraw.run_lucky_draw()

    print("The winner is: ", winner)


'''
TODO

pre 命名规范

3 单元测试

4 封装接口

5 功能测试

6 添加接口功能测试

7 前端设计和开发

8 UI自动化测试
'''