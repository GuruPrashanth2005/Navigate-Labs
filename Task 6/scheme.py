class EvaluationScheme:
    def evaluate(self, marks):
        pass


class PercentageScheme(EvaluationScheme):
    def evaluate(self, marks):
        return sum(marks) / len(marks)


class GradeScheme(EvaluationScheme):
    def evaluate(self, marks):
        avg = sum(marks) / len(marks)
        return "A" if avg >= 80 else "B"


marks = [75, 85, 90]

scheme1 = PercentageScheme()
scheme2 = GradeScheme()

print("Percentage:", scheme1.evaluate(marks))
print("Grade:", scheme2.evaluate(marks))
