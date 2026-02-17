class Config:
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_key(self):
        return self.__api_key


config = Config("SECRET123")
print(config.get_key())
