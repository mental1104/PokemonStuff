'''
Date: 2023-07-01 13:18:03
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 13:23:44
'''
from pydantic import BaseModel

class NatureTuple(BaseModel):
    id: int
    name: str
    decreased_stat: int
    increased_stat: int
