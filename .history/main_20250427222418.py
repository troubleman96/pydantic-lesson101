from pydantic import BaseModel, ValidationError, Field
from typing import List
from enum import Enum


class Gender(str, Enum):
    Male="male"
    Female="female"
    NON_BINARY="Non-Binary"

class Person(BaseModel):
    username:str=Field(default=None,max_length=12)
    email:str
    age:int=Field(lt=30,gt=1)
    friends:List[str]=[]
    gender:Gender



data = {
    "username":"testuser",
    "email":"user@gmail.com",
    "age":"322",
    "friends":["friend01"],
    "gender":Gender.Male

}

try:
    new_person = Person(**data)    

    print(new_person)

except ValidationError as e:
    print(e)
