# rows = 20
# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print(" ")
import pandas as pd

# Refined data (fixed the quotes and added matching elements)
data = {
    "Name": ["Amit", "Raju", "Ravi", "Rakesh"],  # Fixed the typo and added an extra name
    "Age": [10, 55, 44, 30],  # Added the missing age value for Rakesh
    "Salary": [100, 2000, 3000, 2500]  # Added the missing salary value for Rakesh
}

# Creating DataFrame
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
