from pydantic import BaseModel
from typing import list
from enum import Enum


class Gender(str, Enum)

class Person(BaseModel):
    username:str
    email:str
    age:int
    friends:List[str]=[]


data = {
    "username":"testuser",
    "email":"user@gmail.com",
    "age":24
}


new_person = Person(**data)    

print(new_person)

