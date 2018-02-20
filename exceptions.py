class e2eException(BaseException):

    def __init__(self, value):

        self.value = value

    def __str__(self):

        return self.value