class ServiceError(Exception):
    message: str

    def __init__(self, message):
        self.message = message