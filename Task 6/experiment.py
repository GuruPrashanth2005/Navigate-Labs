from datetime import datetime

class Experiment:
    def start(self):
        self.start = datetime.now()
    def end(self):
        self.end = datetime.now()

exp = Experiment()
exp.start()
exp.end()
print(exp.start, exp.end)
