from typing import List
from pydantic.main import BaseModel


class GenerateActivityResponse(BaseModel):
    activity_id: int


class ConfigRequest(BaseModel):
    activity_id: int
    scope: int
    odds: float


class ConfigResponse(BaseModel):
    message: str = "Set successfully!"


class Employee(BaseModel):
    uid: int
    uname: str


class EmployeeList(BaseModel):
    employees: List[Employee]


class AddEmployeeResult(BaseModel):
    status_code: int
    msg: str


class AddEmployeesResponse(BaseModel):
    msg: List[AddEmployeeResult]


class DeleteEmployeeResult(BaseModel):
    status_code: int
    msg: str


class DeleteEmployeesResponse(BaseModel):
    msg: List[DeleteEmployeeResult]


class GenerateWinnerResponse(BaseModel):
    winner_uid: int


if __name__ == '__main__':
    employee1 = {"uid": "88", "uname": "username"}
    employee2 = {"uid": "88", "uname": "username"}
    elist = {"employees": [employee1, employee2]}
    print(Employee(**employee1).json())
    print(EmployeeList(**elist).json())
