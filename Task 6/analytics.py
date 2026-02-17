from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def run(self): pass

class Security(Plugin):
    def run(self): print("Security Running")

class Analytics(Plugin):
    def run(self): print("Analytics Running")

for p in [Security(), Analytics()]:
    p.run()
