from pydantic import BaseModel

class Person(BaseModel):
    username:str
    email:str
    age:int


data = {
    "username":"testuser",
    "email":"user@gmail.com",
    "age":24
}


new_person = Person(**data)    

print(new_person)

