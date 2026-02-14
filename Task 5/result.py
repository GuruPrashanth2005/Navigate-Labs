class Result:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        return "C"

r = Result()
print(r.grade(88))
