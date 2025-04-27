from pydantic import BaseModel
from typing import list

class Person(BaseModel):
    username:str
    email:str
    age:int
    friend:


data = {
    "username":"testuser",
    "email":"user@gmail.com",
    "age":24
}


new_person = Person(**data)    

print(new_person)

