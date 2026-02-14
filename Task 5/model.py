class Model:
    def predict(self, data):
        pass

class LinearModel(Model):
    def predict(self, data):
        return sum(data)

m = LinearModel()
print(m.predict([1,2,3]))
