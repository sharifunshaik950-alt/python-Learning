import matplotlib.pyplot as plt
import numpy as np
x=np.array([4,5,8,9])
y=np.array([7,4,5,6])
plt.plot(x,y)
plt.plot(x,y,marker='*',mfc='b',ms=10,linestyle='dashed',color='r')
plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()