class Plan:
    def bill(self):
        pass

class Monthly(Plan):
    def bill(self):
        return 500

print(Monthly().bill())
