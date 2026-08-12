import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 15, 25, 25])
y = ["AIML", "DS", "ECE", "CSE"]

z = [0, 0, 0.5, 0]

plt.pie(x, labels=y, explode=z, shadow=True)
plt.title("Department-wise Result")
plt.show()
