import matplotlib.pyplot as plt
import numpy as np

# Data for the first subplot (line plot)
x1 = np.arange(0, 11)  # x values from 0 to 10
y1 = 3 * x1 + 2  # y = 3x + 2

# Data for the second subplot (bar chart)
x2 = [1, 2, 3, 4]  # x values
y2 = [10, 20, 25, 30]  # y values

# Creating subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
# First subplot (Line plot)
axes[0].plot(x1, y1, marker='o', linestyle='-', color='g', label='y = 3x + 2')
axes[0].set_title("Line Plot: y = 3x + 2")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True, linestyle='--', alpha=0.7)
axes[0].legend()

# Second subplot (Bar chart)
axes[1].bar(x2, y2, color='b')
axes[1].set_title("Bar Chart")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")

# Adjust layout and show the plot
plt.tight_layout() 
plt.show()