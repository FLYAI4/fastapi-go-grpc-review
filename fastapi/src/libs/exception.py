class CustomHttpException(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        self.error = None


class UserError(CustomHttpException):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(code, message)
