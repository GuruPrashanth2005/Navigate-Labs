import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
carets = np.round(np.random.uniform(0.1, 2.0, 100), 2)
carets.sort()
prices = 3000 * (carets ** 1.5) + np.random.normal(0, 500, 100)
diamonds = pd.DataFrame({'carats': carets, 'price': prices})
print("correlation:", diamonds['carats'].corr(diamonds['price']))
slope, intercept = np.polyfit(diamonds['carats'], diamonds['price'], 1)
print("slope:", slope)  
print("intercept:", intercept)
plt.plot(diamonds['carats'], diamonds['price'])
plt.xlabel('Carats')
plt.ylabel('Price')
plt.title('Diamond Price vs Carats')
plt.show()