from fastapi import FastAPI

from controller.config import create_lucky_draw_activity, set_lucky_draw_config
from controller.employees import Employees
from form.lucky_draw_form import GenerateActivityResponse, ConfigRequest, ConfigResponse, AddEmployeesResponse, EmployeeList, DeleteEmployeesResponse

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.post("/generate-activity/", response_model=GenerateActivityResponse)
async def generate_lucky_draw_activity():
    """
    创建一次抽奖活动
    """

    new_activity_id = create_lucky_draw_activity()
    print("new_activity_id is: ", new_activity_id)

    return GenerateActivityResponse(activity_id=new_activity_id)


@app.post("/set-config/", response_model=ConfigResponse)
async def set_config(request: ConfigRequest):
    """
    基础配置
    """

    set_result = set_lucky_draw_config(request.activity_id, request.scope, request.odds)

    if set_result is True:
        return ConfigResponse()
    else:
        return ConfigResponse(message='Set fail！可能存在重复提交。')


@app.post("/add-employees/", response_model=AddEmployeesResponse)
async def add_employees(request: EmployeeList):
    """
    录入多个员工
    循环添加员工，并把返回结果依次存储到返回信息里
    """
    result_list = []

    for employee in request.employees:
        status_code, msg = Employees.add_employee(employee.uid, employee.uname)
        add_employee_result = {"status_code": status_code, "msg": msg}

        result_list.append(add_employee_result)

    add_employees_response = {"msg": result_list}
    return AddEmployeesResponse(**add_employees_response)


@app.delete("/delete-employees/", response_model=DeleteEmployeesResponse)
async def delete_employees(request: EmployeeList):
    """
    删除多个员工
    """
    result_list = []

    for employee in request.employees:
        status_code, msg = Employees.delete_employee(employee.uid)
        delete_employee_result = {"status_code": status_code, "msg": msg}

        result_list.append(delete_employee_result)

    delete_employees_response = {"msg": result_list}
    return DeleteEmployeesResponse(**delete_employees_response)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
