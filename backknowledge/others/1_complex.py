from enum import Enum
from typing import List, Union
from datetime import date
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Gender(str, Enum):
    man = "man"
    women = "women"


class Person(BaseModel):
    name: str
    gender: Gender


class Department(BaseModel):
    name: str
    lead: Person
    cast: List[Person]


class Group(BaseModel):
    owner: Person
    member_list: List[Person] = []


class Company(BaseModel):
    name: str
    owner: Union[Person, Group]
    regtime: date
    department_list: List[Department] = []

sales_department = {
    "name": "sales",
    "lead": {"name": "Sarah", "gender": "women"},
    "cast": [
        {"name": "Sarah", "gender": "women"},
        {"name": "Bob", "gender": "man"},
        {"name": "Mary", "gender": "women"}
    ]
}

research_department = {
    "name": "research",
    "lead": {"name": "Allen", "gender": "man"},
    "cast": [
        {"name": "Jane", "gender": "women"},
        {"name": "Tim", "gender": "man"}
    ]
}

company = {
    "name": "Fantasy",
    "owner": {"name": "Victor", "gender": "man"},
    "regtime": "2020-7-23",
    "department_list": [
        sales_department,
        research_department
    ]
}

# 初始化自定义的model类型方式一：
company0 = Company(name="cname", owner=Person(name="pname", gender="man"), regtime="2020-7-23",
    department_list=[])
print(company0.json()) # 用双引号
print(type(company0.json())) # str类型，用双引号

print("-----"*6)

# 初始化自定义的model类型方式二：传参一定要带**，通过字典类型来初始化自定义的model类型
company1 = Company(**company) # 通过Company的实例company来创建实例company1

print(company1.json())
print(type(company1.json())) # str类型，用双引号

print(company1)
print(type(company1)) # Company

# 自定义的model类型可以转字典类型
print(company1.dict())
print(type(company1.dict())) # dict

print(jsonable_encoder(company1))
print(type(jsonable_encoder(company1))) # dict

# 其他，同方式一：
company2 = Company(**company1.dict())  # 通过Company的实例转字典类型来创建实例

print(company2.json())
print(type(company2.json())) # str类型，用双引号
