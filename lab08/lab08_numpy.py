import numpy as np

#task 1
hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.zeros(6,int)
unknown_table = np.full((2,3),-1)
identity = np.eye(3)
print(hours.shape,hours.ndim,hours.size,hours.dtype)

#task 2
print(hours[2],hours[-1],hours[2:6],hours[::2],hours[::-1])

