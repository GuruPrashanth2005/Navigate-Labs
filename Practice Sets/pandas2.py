import pandas as pd
# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']}
df = pd.DataFrame(data)
# Get unique values from the 'Department' column
unique_departments = df['Department'].unique()
print("Unique Departments:", unique_departments)