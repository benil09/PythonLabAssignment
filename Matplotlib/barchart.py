import matplotlib.pylab as plt
import numpy as np
import pandas as pd

Months=[
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'may',
    'Jun',
    'Jul',
    'Aug',
    'Sept',
    'Oct',
    'Nov',
    'Dec'
    
]
sales=[
    100,
    120,
    110,
    130,
    125,
    140,
    135,
    145,
    150,
    155,
    160,
    99
]


# plt.figure(figsize=(5,5))

plt.bar(Months,sales,color='red')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales')

#plt.xticks(rotation=45)
#plt.tight_layout()
plt.show()

