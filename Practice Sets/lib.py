import numpy as np
students = np.random.randint(1, 100, size = 5000)
students = np.sort(students)
for i in range(-1,-251,-1):
    print(abs(i), students[i])