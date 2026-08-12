import matplotlib.pyplot as plt
import numpy as np
x=np.array(["c","python","java","c+"])
y=np.array([8,4,10,6])
plt.bar(x,y)
plt.title("mca result")
plt.xlabel("subjects")
plt.ylabel("result")
plt.show()