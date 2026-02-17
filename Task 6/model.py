from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self): pass

class Linear(Model):
    def predict(self):
        print("Linear Prediction")

class Tree(Model):
    def predict(self):
        print("Tree Prediction")

for m in [Linear(), Tree()]:
    m.predict()
