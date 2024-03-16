import array
array4=array.array('i',[100,200,300,400,500])
print("the original array is:\n",array4)
array4[1]=222
array4[2:5]=array.array('i',[333,444,555])
print("the new array is:\n",array4)