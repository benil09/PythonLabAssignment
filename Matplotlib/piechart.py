import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Smartphones=['Samsung','Apple','Realme','Redmi']
shares=[40,30,20,10]

plt.figure(figsize=(7,7))
plt.pie(shares, labels=Smartphones, autopct='%1.1f%%', startangle=90)
plt.title("Smartphones market share")
plt.legend()
plt.show()