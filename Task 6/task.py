from datetime import datetime

class Task:
    def complete(self):
        self.completed_time = datetime.now()
        print("Task Completed At:", self.completed_time)


task = Task()
task.complete()
