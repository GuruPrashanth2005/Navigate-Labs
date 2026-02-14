class Exam:
    def __init__(self, subject, max_marks):
        self.subject = subject
        self.max_marks = max_marks

class Practical(Exam):
    def evaluate(self, marks):
        return marks

e = Practical("AI", 100)
print("Marks:", e.evaluate(85))
