class Engine:
    def run(self, data):
        return max(data)

e = Engine()
print(e.run([5,2,8]))
