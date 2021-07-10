from enum import Enum
from typing import Optional, List
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



class PageRequest(BaseModel):
    """
    特殊处理：不要问为什么是驼峰，为了和公司规范、和前端同学规范对齐
    """
    pageSize: int = 20
    page: int = 1


class PageResponse(BaseModel):
    total: int
    current: int
    size: int


class PatchResponse(BaseModel):
    message: str = "OK"
    code: int = 1


class OperateType(str, Enum):
    KILL = "kill"
    RETRY = "retry"


class TaskStatus(int, Enum):
    FAILED = 0
    RUNNING = 1
    WAITING = 2
    SUCCESS = 3


class OverWrite(int, Enum):
    FALSE = 0
    TRUE = 1


class LoadHive(BaseModel):
    file_name: str
    file_uuid: str
    hive_table: str
    overwrite: int = OverWrite.TRUE
    fields_split: Optional[str] = ","
    collection_split: Optional[str] = "|"
    map_split: Optional[str] = ":"


class CreateTaskRequest(LoadHive):
    pass


class CreateTaskResponse(LoadHive):
    id: int
    created_time: Optional[str] = "2021-01-19T16:31:23"
    end_time: Optional[str] = None
    status: int


class OperateTaskRequest(BaseModel):
    operate_type: str


class ListTasksResponse(BaseModel):
    records: List[CreateTaskResponse]
    page: PageResponse
