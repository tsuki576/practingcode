from array import array
array5=array('i',[20,25,30,25,40,60,55,25,35,45,40,25])
print("the length of the array is:\n",array5)
print("the length of the array is:",len(array5))
print("min value:",min(array5))
print("max value:",max(array5))
print("element 25 occured",array5.count(25),"times")
array5.append(55)
newarray5=array('i',[11,22,33])
array5.extend(newarray5)
array5.insert(3,45)
print("the new array is:\n",array5)
print("the last element",array5.pop(),"is removed")
mylist=array5.tolist()
print("the list formed from an array is:\n",mylist)