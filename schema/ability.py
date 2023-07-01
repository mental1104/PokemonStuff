'''
Date: 2023-07-01 13:16:12
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 13:16:21
'''
from pydantic import BaseModel

class AbilityTuple(BaseModel):
    id: int
    name: str

    