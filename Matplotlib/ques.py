import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Plot two lines on the same graph:
#	•	Line 1: y = 2x for x from 0 to 5.
#	•	Line 2: y = x^3 for x from 0 to 5.


x1=np.arange(0,6)
x2=np.arange(0,6)

y1=2*x1
y2=x2**3

plt.figure(figsize=(7,8)) #creates a canvas for the plotting of the above equation
plt.plot(x1,y1,marker='o',linestyle='-',label='y=2*x',color='g')
plt.plot(x2,y2,marker='o',label="y2=x2**3",linestyle='-',color='r')

plt.title("showing two equation simultaneously")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True,linestyle="--",alpha=0.4)
plt.show()