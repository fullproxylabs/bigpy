class _Base:

    def __init__(self, response_data: dict):

        for key, value in response_data.items():
            setattr(self, key, value)

    def __str__(self):

        return str(self.__dict__)