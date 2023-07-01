'''
Date: 2023-07-01 00:13:54
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 16:24:04
'''

from typing import Optional
from pydantic import BaseModel

class PokemonTuple(BaseModel):
    id: int
    name: str
    HP: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    type1: int
    type2: Optional[int]
    ability1: int
    ability2: Optional[int]
    hidden_ability: Optional[int]

    