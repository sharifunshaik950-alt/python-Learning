import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3])
y=([0.5,1.5,2.5,4.8])
z = [1, 2, 1]   

plt.hist(x, bins=3, weights=z, edgecolor='black')

plt.title("Histogram Plot")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
