from pydantic import BaseModel
from typing import Optional, List


class Address(BaseModel):
    street: str
    number: int
    zipcode: int


class Person(BaseModel):
    first_name: str
    last_name: str
    interest: Optional[List[str]]


address_data = {"street": "Main street", "number": 1, "zipcode": 12345}
address = Address.parse_obj(address_data)
data = {"first_name": "Ahmed", "last_name": "Besbes", "address": address}
print(address)
person = Person.parse_obj(data)
print(person)
