import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plot a line graph showing the relationship between x (from 0 to 10) and y = x^2.

# Data preparation
x = np.arange(0, 11)  # x values from 0 to 10
y = x**2  # y = x^2

# Plotting
plt.figure(figsize=(7,8)) #creates a new canvas for plotting

plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x^2')  # Line graph with markers
plt.title("Line Graph of y = x^2", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc="upper left")
plt.show()


