emp_dict["age"]=40
print("the key value pairs in the dict after modifying age are:\n",emp_dict.items())
emp_dict["address"]="pune"
emp_dict.update({"gender":"male"})
emp_dict.setdefault("qualification","mba")
print("the key-value pairs in dictionary after adding new key-value pairs are:\n",emp_dict.items())
print("the value of designation key is:",emp)