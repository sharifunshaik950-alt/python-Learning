import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,1,2,1]
x1=[2,3,4,5,6]
y1=[6,6,3,4,5]
plt.scatter(x,y,label="girls",color='r')
plt.scatter(x1,y1,label="boys",color='b')
plt.title("results of boys & girls")
plt.xlabel("girls & boys")
plt.ylabel("marks")
plt.show()
