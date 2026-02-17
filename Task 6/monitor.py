from datetime import datetime

class Monitor:
    def record(self):
        time = datetime.now()
        print("Execution Time:", time)


monitor = Monitor()
monitor.record()
