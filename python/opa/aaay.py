import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
print([a])
print(a.sum())
print(a.min())
print(a.max())
print(a.sum(axis= 0))
print(a.sum(axis=1))
print(a.cumsum(axis= 0 ))
print(a.cumsum(axis= 1))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
#2
#find the sol -3x + y = 9 and x + 2y =8 
# linear algerbric 
import numpy as np 
a=np.array([[3,1],[1,2]])
b=np.array([9,8])
x=np.linalg.solve(a,b)
print(x)