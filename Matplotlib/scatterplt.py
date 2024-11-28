import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

age=[22, 25, 30, 35, 40]
salary=['25k','30k','20k','22k','40k']
salary.sort()

plt.scatter(age,salary,color='blue',marker='o')
plt.title('Salary with given age group')
plt.xlabel('age')
plt.ylabel('salary')
plt.show()