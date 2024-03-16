mylist12=[10,20,30,40,30,30,50,60,70,30]
print("the number of times 30 occured:",mylist12.count(30))
print("the position of 20 value:",mylist12.index(20))
print("the max value:",max(mylist12))
print("the min value:",min(mylist12))

mylist12.remove(60)
print("the new list after 60:\n",mylist12)

mylist12.append(222)
print()

mylist12.insert(5,12)
print("the new list after adding element 12 at an index before 5 is:\n",mylist12)

print("the last element of list is:",mylist12.pop())
print("the fifth element of list is:",mylist12.pop(4))

print("the length of the new list is:",len(mylist12))

print("the sum of all elements in new list is:",sum(mylist12))

mylist12.reverse()
print("the reversed list is :\n",mylist12)
print("the sorted list without modifying the list is:\n",sorted(mylist12))

mylist13=mylist12.copy()

templist=list([1,2,3])
mylist13.extend(templist)
print("the extended new list:\n",mylist13)

mylist13.clear()
print(mylist13)
print("the new list is:",mylist13)