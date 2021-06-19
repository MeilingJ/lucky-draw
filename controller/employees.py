
from model.employee import Employee
'''
员工类，员工录入和删除 employee：add_employee， delete_employee
'''


class Employees:

    employees = []  # 员工列表 [(员工号, 员工名),(员工号, 员工名),...]


    def add_employee(self, uid, uname):
        '''
        查询员工号是否存在员工表里；
        如果不存在则添加并存储则员工表里 1
        如果员工号存在，但用户名不一致，则报错"员工号已存在，但员工姓名跟系统里的员工姓名不一致，请核实录入信息！" 2
        如果员工号存在，且用户名也一致，则不重复添加；1
        :param employee: (员工号，员工姓名)
        :return: status_code，msg
        '''
        # e = Employee()
        # employee_data = Employee(uid='8', uname='aj', status='在职')
        self.employees.append(employee)

    def delete_employee(self, employee):
        '''
        检查该员工号是否在员工列表中存在
        如果员工号存在，且用户名也一致，则在数据库删除；1
        如果员工号存在，但用户名不一致，则报错"该员工号存在，但员工姓名跟系统里的员工姓名不一致，请检查并重新操作！" 2
        如果不存在, 则报错"该员工号不存在，请检查并重新操作！" 2
        :param employee:
        :return: status_code，msg
        '''
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("The employee is not in the luckydraw system!")


if __name__ == "__main__":
    es = Employees()
    e = (3, 'amity')
    es.add_employee(e)
    print(es.employees)


    es.delete_employee(e)
    print(es.employees)

    es.delete_employee(e)
    print(es.employees)
