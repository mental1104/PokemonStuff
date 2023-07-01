'''
Date: 2023-07-01 13:17:30
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 15:20:19
'''
from pydantic import BaseModel

class TypeTuple(BaseModel):
    id: int
    name: str
    zero: list
    low: list
    medium: list
    high: list
    