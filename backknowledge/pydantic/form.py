"""
@File    : form.py
@Time    : 2021/1/24 12:37 上午
@Author  : huangqing
@Project : htc
"""
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class TypeFormat(str, Enum):
    fixed = "fixed"
    digit = "digit"
    range = "range"

class SupportedType(BaseModel):
    key: str
    name: str
    type: Optional[TypeFormat] = TypeFormat.fixed
    unit: Optional[str] = None

support_type = {
    "key": "akey",
    "name": "aname",
    "type": "fixed",
    "unit": "this is unit"
}

s = SupportedType(**support_type)
print(s.json())

class SupportedTypeList(BaseModel):
    records: List[SupportedType] = list()

support_type_list = {
    "records": [support_type]

}

s = SupportedTypeList(**support_type_list)
print(s.json())



class TypeRequest(BaseModel):
    key: str
    params: Optional[List[int]]

type_request = {
    "key": "akey",
    "params": ["2","3"]
}
s = TypeRequest(**type_request)
print(s.json())

columns = [{
    "key": "phone_number",
    "params": None
}]
s = TypeRequest(**columns[0])
print(s.json())


class GenerateRequest(BaseModel):
    fileName: str
    rowCount: int
    types: List[TypeRequest]


generate_request = {
    "fileName": "afilename",
    "rowCount": 2,
    "types": [
        type_request,
        type_request]
}
s = GenerateRequest(**generate_request)
print(s.json())
