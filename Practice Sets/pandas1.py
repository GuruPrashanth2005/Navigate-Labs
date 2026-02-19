import pandas as pd
import numpy as np
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
ages = [25, 30, 35, 40, 45]
data = pd.DataFrame({'Name': names, 'Age': ages})
mean_age = np.mean(data['Age'])
print(data)
print("Mean Age:", mean_age)
print(data['Age'] >= mean_age)