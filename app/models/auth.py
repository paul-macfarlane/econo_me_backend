from pydantic import BaseModel, model_validator, EmailStr, field_validator


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

    @field_validator("password")
    def password_secure(cls, value):
        errors = []

        if len(value) < 8:
            errors.append("Password must be at least 8 characters long")

        if not any(char.isdigit() for char in value):
            errors.append("Password must contain at least one digit")

        if not any(char.isalpha() for char in value):
            errors.append("Password must contain at least one letter")

        if not any(char.isupper() for char in value):
            errors.append("Password must contain at least one uppercase letter")

        if not any(char.islower() for char in value):
            errors.append("Password must contain at least one lowercase letter")

        if errors:
            raise ValueError(errors)

        return value

    @model_validator(mode="after")
    def passwords_match(self, values):
        if self.password != self.confirmPassword:
            raise ValueError("Passwords do not match")
        return self
