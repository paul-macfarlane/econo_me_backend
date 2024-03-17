from pydantic import BaseModel, model_validator, EmailStr


class Token(BaseModel):
    accessToken: str
    tokenType: str


class Login(BaseModel):
    email: EmailStr
    password: str


class SignUp(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str

    @model_validator(mode="after")
    def passwords_match(self, values):
        if self.password != self.confirmPassword:
            raise ValueError("Passwords do not match")
        return self
