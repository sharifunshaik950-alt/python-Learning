import numpy as np
arr=np.array([2,3,4])
x=arr.view()
arr[0]=90
print(arr)
print(x)