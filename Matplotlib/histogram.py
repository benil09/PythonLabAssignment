import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


np.random.seed(10)
marks=np.random.randint(0,101,50)
print(marks)

plt.figure(figsize=(7,7))

plt.hist(marks,bins=10,range=(0,100),edgecolor='black',alpha=0.4)
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.xticks(ticks=np.arange(0, 101, 10))
plt.yticks(ticks=np.arange(0, 10,1))
plt.grid( linestyle='--', alpha=0.7)
plt.legend()
plt.show()

