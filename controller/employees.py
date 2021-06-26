
from model.lucky_draw_employee import Lucky_draw_employee
from utils.connect_db import engine, session
'''
员工类，员工录入和删除 employee：add_employee， delete_employee
'''


class Employees:

    employees = []  # 员工列表 [(员工号, 员工名),(员工号, 员工名),...]

    def add_employee(self, id, name):
        '''
        查询员工号是否存在员工表里；
        如果不存在则添加并存储则员工表里 1
        如果员工号存在，但用户名不一致，则报错"员工号已存在，但员工姓名跟系统里的员工姓名不一致，请核实录入信息！" 2
        如果员工号存在，且用户名也一致，则不重复添加；1
        :param employee: (员工号，员工姓名)
        :return: status_code，msg
        '''

        result = session.query(Lucky_draw_employee).filter_by(uid=id).first()
        print("查询某员工id的结果：", result)

        status_code = 0
        msg = ''

        if result is None:
            employee_data = Lucky_draw_employee(uid=id, uname=name, status='在职')
            session.add(employee_data)
            session.commit()
            status_code = 1
            msg = '员工已添加'
        elif result.uid == id and result.uname == name:
            status_code = 1
            msg = '员工已经存在，不需要重复添加！'
        elif result.uid == id and result.uname != name:
            status_code = 2
            msg = '员工号已存在，但员工姓名跟系统里的员工姓名不一致，请核实录入信息！'

        return status_code, msg

    def delete_employee(self, id):
        '''
        检查该员工号是否在员工列表中存在
        如果员工号存在，则在数据库删除；1
        如果不存在, 则报错"该员工号不存在，请检查并重新操作！" 2
        :param employee:
        :return: status_code，msg
        '''
        result = session.query(Lucky_draw_employee).filter_by(uid=id).first()
        print("查询某员工id的结果：", result)

        status_code = 0
        msg = ''

        if result is not None:
            session.delete(result)
            session.commit()
            status_code = 1
            msg = '员工已删除'
        else:
            status_code = 2
            msg = '该员工号不存在，可能已删除！'

        print(status_code, msg)


if __name__ == "__main__":
    es = Employees()
    result = es.add_employee(90, 'a3')
    print(result)

    es.delete_employee(91)

    # es = Employees()
    # e = (3, 'amity')
    # es.add_employee(e)
    # print(es.employees)
    #
    #
    # es.delete_employee(e)
    # print(es.employees)
    #
    # es.delete_employee(e)
    # print(es.employees)
