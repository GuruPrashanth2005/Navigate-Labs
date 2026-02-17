class Workout:
    def calculate_calories(self):
        pass


class Running(Workout):
    def calculate_calories(self):
        return 300


class Cycling(Workout):
    def calculate_calories(self):
        return 250


workouts = [Running(), Cycling()]

for w in workouts:
    print("Calories Burned:", w.calculate_calories())
