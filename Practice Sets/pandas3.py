import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
budgets = np.random.uniform(10, 300, 50) 
revenues = budgets * np.random.uniform(1.2, 4.0, 50) + np.random.normal(0, 20, 50)

movies = pd.DataFrame({
    "Budget (Million USD)": budgets,
    "Revenue (Million USD)": revenues
})

plt.figure()
plt.scatter(movies["Budget (Million USD)"], movies["Revenue (Million USD)"])
plt.xlabel("Movie Budget (Million USD)")
plt.ylabel("Movie Revenue (Million USD)")
plt.title("Relationship Between Movie Budget and Revenue")
plt.show()
