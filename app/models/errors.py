class ModelNotFoundError(Exception):
    code = 404

    def __init__(self, model: str, id: str):
        self.message = f"{model} with id {id} not found"
        super().__init__(self.message)
