from pydantic import BaseModel


class User(BaseModel):
    email: str = None
    password: str = None


    def set_email(self, email):
        self.email = email


x = User()

x.set_email('dskldjskd')
print(x.email)

print(x.json(indent=4))