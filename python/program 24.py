#1 

import numpy
array1=numpy.array([1,2,3,4,5,6],int)
print("The integer array is:\n",array1)
array2=numpy.array(["a","b","c","d","f"])
print("The character array is:\n",array2)
array3=numpy.array(["JK","MH","UP","TN"],dtype=str)
print("The string array is:\n",array3)
array4=numpy.array([1,2,3,4,5,6],dtype=float)
print("The integer array is:\n",array4)
print()

#2

newarray=numpy.array([30,40,20,30,10,80,60,40,80],int)
newarray[4]=45
print("The new array is: \n",newarray)
print()
print('The size of the array is:',newarray.size)
print()
print('The datatype of the array is:',newarray.dtype)
print()
print('The minimum of the array is:',numpy.min(newarray))
print()
print('The maximum of the array is:',numpy.max(newarray))
print()
print('The sum of the array is:',numpy.sum(newarray))
print()
print('The product of the array is:',numpy.prod(newarray))
print()
print('The mean of the array is:',numpy.mean(newarray))
print()
print('The median of the array is:',numpy.median(newarray))
print()
print('The Standard Deviation of the array is:',numpy.std(newarray))
print()
print('The Variance of the array is:',numpy.var(newarray))
print()
