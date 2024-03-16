
student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
    print(student_marks)
#2
#Used to calculate total operation time
list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
#3
#Used to calculate total operation time
#Importing Numpy
from matplotlib import pyplot as plt
from networkx import johnson
import numpy as np
#Creating a numpy array of 1 million numbers

import numpy as np
student_marks_arr = np.array([78, 92, 36, 64, 89])
print(student_marks_arr)
#4
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
horsepower_arr
print(horsepower_arr)
#4
#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from car_attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr)
#5
#creating a list of lists of  mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr.shape)
#Here, 3 represents the number of rows and 5 represents the number of elements in each row.
#6
#creating a list of lists of  mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#creating a numpy array from attributes list
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr.dtype)
#7
#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#converting dtype
car_attributes_arr = np.array(car_attributes, dtype = 'float')
print(car_attributes_arr)
print(car_attributes_arr.dtype)
#8
#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing the second car from the array
print(cars[1])
#9
#Creating a 2D array consisting car names and horsepower
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
car_hp_arr = np.array([car_names, horsepower])
print(car_hp_arr)
#10
#creating an array of cars
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
#accessing a subset of cars from the array
print(cars[1:4])
#11
#Creating a 2D array consisting car names, horsepower and acceleration
car_names = ['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino']
horsepower = [130, 165, 150, 150, 140]
acceleration = [18, 15, 18, 16, 17]
car_hp_acc_arr = np.array([car_names, horsepower, acceleration])
print(car_hp_acc_arr[0:3,0:3])
#mean
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#mean horsepower
print("Mean horsepower = ",np.mean(horsepower_arr))
#median
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#median horsepower
print("Median horsepower = ",np.median(horsepower_arr))
#min & max
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
print("Minimum horsepower: ", np.min(horsepower_arr))
print("Maximum horsepower: ", np.max(horsepower_arr))
print(" index of Minimum horsepower: ", np.argmin(horsepower_arr))
print("index of Maximum horsepower: ", np.argmax(horsepower_arr))
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
x = np.where(horsepower_arr >= 150)
print(x) # gives the indices 
# With the indices , we can find those values 
horsepower_arr[x]
#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#creating filter array
filter_arr = horsepower_arr > 135
newarr = horsepower_arr[filter_arr]
print(filter_arr)
print(newarr)
#sorting the array
horsepower = [130, 165, 150, 150, 140]
horsepower_arr = np.array(horsepower)
print('orignal array',horsepower_arr)
horsepower_arr.sort()
print('orignal array after sort ',horsepower_arr)
#The difference is that the array.sort() function
# modifies the original array by default, whereas the sort(array) function does not.

#The mathematical operations can be performed on Numpy arrays. Numpy makes use of optimized,
 #pre-compiled code to perform mathematical operations on each array element. This
 #eliminates the need of using loops, thereby enhancing the performance. This process
#is called vectorization.

#Numpy provides various mathematical functions such as sum(), add(), sub(), log(), sin() etc. 
#which uses vectorization.
#sum()
student_marks_arr = np.array([78, 92, 36, 64, 89])
print('sum of the numbers',np.sum(student_marks_arr))
additional_marks = [2, 2, 5, 10, 1]
student_marks_arr += additional_marks
print(student_marks_arr)
#boardcasting 
import numpy as np
# Array 1
array1=np.array([5, 10, 15])# larger array
# Array 2
array2=np.array([5])# small array 
array3= array1 * array2 
print(array3)
#Students marks in 4 subjects
students_marks = np.array([[67, 45],[90, 92],[66, 72],[32, 40]])
#Broadcasting
students_marks += [5,10]
print(students_marks)
#matrix

#appendix
##Arange
#This method returns evenly spaced values between the given intervals excluding the end limit. 
#The values are generated based
#on the step value and by default, the step value is 1.
#start and end limit
arrange_arr=np.arange(0,10000)

print(arrange_arr)
#step 2
#step value = 2
arrange_arr1=np.arange(0,10,2)

print(arrange_arr1)
#Linspace
#Generating values between 0 and 10
arr = np.linspace(0,10)
print(arr)
print('Length of arr: ',len(arr))
#Number of values = 3
print(np.linspace(0,10,3))
#Zeroes and Ones
#zeros
x=np.zeros(5)
print(x)
#2D
y=np.zeros([2,3])
print(y)
#Full and Eye
#full
#number=5, value=8
z=np.full(5,8)
print(z)
#shape=[3,3], value=numpy
j=np.full([3,3],'numpy')
print(j)
#3x3 identity matrix
eye_arr=np.eye(3)
print(eye_arr)
#Random
#NumPy has numerous ways to create random number arrays.
# Random numbers can be created for the required length, from a uniform distribution 
#by just passing the value 
#of required length to the random.rand function.
x=np.random.rand(5)
print(x)
#random integer values low=1, high=10, number of values=5
x=np.random.randint(1,10, size=5)
print(x)
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([100,200,300,400,500])
print(np.add(arr1, arr2))
#numpy exercise 
steps_arr= np.array([6012,7079,6886,72304598,5564,6971,7763,8032,9569])
#panda 
#1
import pandas as pd 
series = pd.Series(data = [78, 92, 36, 64, 89])  
print(series.index)
#2 Accessing data in series:
import pandas as pd 
series = pd.Series(data = [78, 92, 36, 64, 89])  
print(series.values)
#3 Slicing a series:
import pandas as pd 
series = pd.Series(data = [78, 92, 36, 64, 89])  
print(series[1:3])
#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
print(car_price)
#5 2D data frame

car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_man_dict = {'Swift': 'maruti' ,
                       'Jazz' :  'honda',
                       'Civic' : 'honda',
                       'Altis' : 'toyota',
                       'Gallardo': 'lamborgini'
                      }
car_man = pd.Series(car_man_dict)
print(car_man)
print(car_price)
cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
print(cars)

#. From a single series object
#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
print(car_price)
#Creating a DataFrame from car_price Series
pd.DataFrame(car_price, columns=['Car Price'])
#
data = [{'name':'Subodh','marks':28},
{'name':'Ram','marks':27},
{'name':'Abdul','marks':26},
{'name':'john','marks':28}]
print(pd.DataFrame(data))
#
#Using dictionary to create a series
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)
car_man_dict = {'Swift' : 'Maruti',
                  'Jazz'   : 'Honda',
                  'Civic'  : 'Honda',
                  'Altis'  : 'Toyota',
                   'Gallardo' : 'Lamborghini'}
car_man = pd.Series(car_man_dict)
cars = pd.DataFrame({'Price': car_price , 'Manufacturer' : car_man})
print(cars)
#




























    
