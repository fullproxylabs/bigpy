class _Base:

    def __init__(self, bigip, response_data: dict):

        self.bigip = bigip
        for key, value in response_data.items():
            setattr(self, key, value)

    def __str__(self):

        return str(self.__dict__)