import array

array1=array.array("i",[5,6,7,8,9,10])
print("the array elements are:")
for element in array1:
    print("the element is:",element)
print("creating a unicode array")
array2=array.array("u",["a","b","c","d"])
for element in array2:
    print("the element is:",element)