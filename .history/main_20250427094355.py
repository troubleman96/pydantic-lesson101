from pydantic import BaseModel, ValidationError
from typing import List
from enum import Enum


class Gender(str, Enum):
    Male="male"
    Female="female"
    NON_BINARY="Non-Binary"

class Person(BaseModel):
    username:str
    email:str
    age:int
    friends:List[str]=[]
    gender:Gender



data = {
    "username":"testuser",
    "email":"user@gmail.com",
    "age":"24",
    "friends":["friend01"],
    "gender":Gender.Male

}

try:
    new_person = Person(**data)    

    print(new_person)

except ValidationError as e:
    print(e)
