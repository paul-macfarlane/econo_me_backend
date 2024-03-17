class UnauthenticatedErrorException(Exception):
    code = 401

    def __init__(self):
        self.message = "Unauthenticated"
        super().__init__(self.message)


class ModelNotFoundException(Exception):
    code = 404

    def __init__(self, model: str, id: str):
        self.message = f"{model} with id {id} not found"
        super().__init__(self.message)


class ResourceAlreadyExistsException(Exception):
    code = 409

    def __init__(self, model: str, id: str):
        self.message = f"{model} with id {id} already exists"
        super().__init__(self.message)


class UserAlreadyExistsException(Exception):
    code = 409

    def __init__(self, email: str):
        self.message = f"User with email {email} already exists"
        super().__init__(self.message)
