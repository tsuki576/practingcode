tuple1=()
print(type(tuple1))
print("an empty tuple is:",tuple1)

tuple2=(42,)
print("a tuple with single element is:",tuple2)

tuple3=(1,2,3,4)
print("a tuple with multiple element is:",tuple3)

tuple4=tuple(range(5,50,5))
print("a tuple created using range function is:\n",tuple4)

list_example = [10,20,30,40,50]
tuple5=tuple(list_example)
print("a tuple is created from a list is:\n",tuple5)