from pydantic import BaseModel


class UserOutput(BaseModel):
    name: str
    email: str


class User(UserOutput):
    password: str

# Наружу давать данные UserOutput, в БД хранить User
