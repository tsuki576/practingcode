import numpy as np 
newarray2=np.reshape(range(10,50,2),(4,5))
print("the complete multidemensional is:\n",newarray2[:,:])
print("the first row is:\n",newarray2[0:1])
print("the third and fourth rows are:\n",newarray2[2:4])
print("the elements at first and second of both row and coloumn are:\n",newarray2[0:2,0:2])
print("the elements in second to fouth row and second to third coloumn are:\n",newarray2[1:4,1:3])