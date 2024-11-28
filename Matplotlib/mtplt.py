import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data ={
    "Bat":["SG","MRF","spartan","SS"],
    "price":[1200,2300,1100,1000],
    "weight":[1000,1200,900,1300]
}



dataframe=pd.DataFrame(data)
plt.plot(dataframe["price"],dataframe["weight"])
plt.xlabel("batPrice")
plt.ylabel("batWeight")

plt.title("Bat price depends on the weight")
plt.show()