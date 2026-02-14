class Storage:
    def __init__(self, limit):
        self.limit = limit

s = Storage(1000)
print("Limit:", s.limit)
