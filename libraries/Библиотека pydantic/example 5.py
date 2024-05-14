from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    balance: float = 0


new_user = User(
    username='Владислав',
    email='masavnik@ya.ru',
    balance=10000
)

print(new_user.json())
print(new_user.dict()['username'])