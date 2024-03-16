#1

import array
array3=array.array('i',[10,20,30,40,50,60,70,80])
print("The first result is:",array3[1:4])
print("The second result is:",array3[:2])
print("The third result is:",array3[3:])
print("The fourth result is:",array3[-3:])
print("The fifth result is:",array3[:-6])
print("The sixth result is:",array3[1:6:2])
print("The sixth result is:",array3[0:7:3])
print("The last value is:",array3[::4])
print()

#2

array4=array.array("i",[100,200,300,400,500])
print("The original array is:\n",array4)
print()
array4[1]=222
array4[2:5]=array.array("i",[333,444,555])
print("The new array is:\n",array4)
print()

#3

from array import array
array5=array('i',[20,25,30,25,40,60,55,25,35,45,40,25])
print('The length of the array is:\n',array5)
print('The length of the array is:\n',len(array5))
print("Min value:",min(array5))
print("Max value:",max(array5))
print("Element 25 occured",array5.count(25),"times")
array5.append(55)
newarray5=array('i',[11,22,33])
array5.extend(newarray5)
array5.insert(3,45)
print("The new array is:\n",array5)
print("The last element ",array5.pop(),"is removed")
mylist=array5.tolist()