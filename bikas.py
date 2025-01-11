# # # print("Hello I am learning python.", " I am the only one molecualr biologist of Nepal in the field of molecular and compuational genetics")
# # # #variable simply defines as which value is varies constantly, python assigned the value from left to right in a variable
# # # print(35)
# # # name = ("Bikas")
# # # age = 24
# # # value = 6.494298498
# # # context = None
# # # print(name, age)
# # # print("My  name is:", name)
# # # print("My age is: ", age)
# # # age2 = age
# # # #To identify the types of data
# # # print("My age is :", age2)
# # # print(type(age))
# # # print(type(name))
# # # print(type(value))
# # # print(type(context))
# # # ################ Ttypes of operator in python
# # # a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# # # b = -12
# # # result = a + b
# # # print(result)
# # # ###########arthematic operator in python 
# # # print(a%b)
# # # Bikas = 50 
# # # Umisha = 100 
# # # print(Bikas**Umisha)#this is for power opearion 
# # # print(Bikas!=Umisha)
# # # print(Bikas==Umisha)
# # # ##########taking the input data from the users 
# # # # name= input("enter your name:")
# # # # age=input("enter your age: ")
# # # # place=input("where are you from:")
# # # # print("your name and age is:",name, age, place)
# # # # side=float(input("Enter the side of the squre:"))
# # # # print("The area of the room is:", side*side)
# # # #########Chapter one closed###
# # # #chapter two for creating the next line in the python
# # # Nepal="Nepal is the hotspot country for the biodiversity.\n where tremandious amount of flora and funa species are existed"
# # # print(Nepal)
# # # #iNDEXING in pyhton this helps to access the charcter value of the string 
# # # str= "Bikas Basnet"
# # # print(str[5])
# # # ###slicing in python which is essential for the machine learning algorithem
# # # print(str[-5:-2])
# # # Bikas= "I am developing Molecular biologist"
# # # print(Bikas.endswith("biologist"))
# # # #########test for developing the calculator
# # # # Num1=input("Enter a number")
# # # # Num2=input("Enter another number")
# # # # print("Your result is", Num1+Num2)
# # # #To capitalize the string
# # # Rupa=("rupa is name of my mother")
# # # print(Rupa.capitalize())
# # # ###To find and replaced the 
# # # print(Rupa.capitalize(), Rupa.replace("mother", "heart"))
# # # ###Find str.find function in pyhton 
# # # print(Rupa.find("my"))#Indexing not be negative value
# # # Sobit= "My father name is sovit man Basnet"
# # # print(Sobit.count("s"))
# # # ###Questions
# # # Fstname= input("Enter your first name")
# # # print("length of your name is:", len(Fstname))
# # # # print(Fstname.count("$"))
# # # ##Conditional statement in python if , elif and else: 
# # # # age = 12
# # # # if (age >= 18):
# # # #     print("This candidate is allowed for the votting purpose")
    
# # # ###Creating the traffic light rules for the pedestrains
# # # # color = "Pink"

# # # # if color == "Green":
# # # #     print("You need to wait because some people are on the road")
# # # # elif color == "red":
# # # #     print("Have a safe journey")
# # # # else:
# # # #     print("You need to look Trafic")

# # ##Assinging the grade of the student
# # Grade= int(input("Enter your obtained marks:"))

# # if (Grade>=90):
# #    Grade="A"
# # elif (Grade>=80 and Grade<90):
# #     Grade="B"
# # elif(Grade>60 and Grade<80):
# #     Grade="C"
# # else:
# #     Grade="E"
# # print("Grade of the student is:", Grade)
# # ###Nesting in the python: writting the case within the same case
# # age = int(input("Enter your age: "))  # Convert input to an integer

# # if age >= 18 and age < 90:
# #     category = "Suitable age"
# # elif age >= 90:
# #     category = "You are over matured"
# # else:
# #     category = "You are in the right place"

# # print("Categories of voter:", category)
# # SL= int(input("Number of publication in Q1"))
# # if (SL >= 5):
# #     decision="accept"
# # elif(SL<5):
# #     decision="needs revsion"

# # # print("Due to your limited publication decison is:", decision)
# # num=int(input("Enter any number"))
# Color = "RED"
# if Color== "RED":
#  decision= "You need to waait"
# elif Color!="RED":
#     decision="You need to see Traffic"
# print(decision)


# # case= 14
# # rem=case%2
# # if(rem==0):
# #     print("Even")
# # else:
# #     print("Odd")
# ####LIst in pyhton
# Bikas=[12, "Maize", 678]
# Bikas.append(512)
# print(Bikas)
# ##########Lists sorts 
# Tharu=[9,8,7,6,5,4,2,1,3]
# Tharu.append(-5)
# Tharu.sort(reverse=False)
# Tharu.pop(3)
# print(Tharu)

############lectured 4 ###############
###Dictionary in pyhton
# info={
#     "Name": "Bikas",
# "CGPA": 4,
# "Marks": [90,95,100]}
# print(info)
#######loops in python 

# Num = 0
# while Num <= 100:  
#     print("The sequence of the number is", Num)
#     Num += 1 
###
# Name= input("Enter your Name")
# AGE= float(input("Enter your AGE"))
# print(f"My name is {Name} and My age is{AGE}")##Thi is the new style of writitng 
# print("My name is", Name, "and My age is", AGE)###This is old style of writting the commands in python


# i= 0 
# while i<=50:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=0
####For loops in python
# Bik = "I am in Bhimnagar"
# for char in Bik:
#     if char == "a":  # Fix: Compare to the character 'a'
#         break
#     print(char)
# else:
#     print("Session is ended")
# nums=[1,2,4,6,7,9,10]
# for el in nums:
#     print(el)
###Counting the varibale index in list
# my_list = ["Bikas", 23, 45, "Roshan", "Bhimnaga", 84]
# x = "Roshan"
# for index, el in enumerate(my_list):
#     if el == x:
#         print("Given string is found at index:", index)

####For int fouding in the tupples
# ram = (1, 2, 4, 4, 4, 4, 5, 6, 7, 3, 4, 7, 9, 6, 5, 7, 7, 7, 74, 4, 5, 654, 45)
# x = 4
# idx = 0
# for el in ram:
#     if el == x:
#         print("Given integer is found at index:", idx)
#     idx += 1
###Using the estimation of range in  the functions, here 2 indicates the start function and 100 in ends functions 

# for i in  range(2,100):
#     print(i)#########
# for i  in range(2, 20, 5):# here 2 is start , 20 is end and 5 is range  gap between
#     print(i)
#For multiplication table
# Num = int(input("Enter a number :"))
# for i in range(1* 20):
#     print(Num * i)
###Used of pass function in code 
# for i in range(30):
#     pass
# print("This portion is left for the coding")

# n= int(input("Enter a number :"))
# i = 1
# while i <=10:
#     print (n*i)
#     i+=1
# Bikas=[1,2,7,6,8,9,3]
# for el in Bikas:
#     print(Bikas)
#####This chapter wrapped the lecture 5 of the python
###Chapter six in python: functions and Recursions, Thoery ,concept ##
#We can perform the severeal same task again and again from the given functions  while loops can be terminated 
# def calcu_Sum(a, b):
#     result = a + b  # Renamed the variable from sum to result
#     print(result)
#     return result

# # Test cases
# calcu_Sum(2500, 45000)
# calcu_Sum(6000, -45000)
# def cal_min(a,  b):
#     result= a-b
#     print(result)
#     return result


# # cal_min(100, -60)
# def cal_aver(a, b, c):
#     SUM= a+ b+c
#     avg= SUM/3
#     print(avg)
#     return(avg)
 
# cal_aver(450, 650, 867)
# print("Hello I am from Nepal", end= "")
# print("I love you very much")
###Recusrion in pyhton
# def fac_cal(n):
#     if n == 0:  # base case
#         return 1  # factorial of 0 is 1
#     else:
#         return n * fac_cal(n-1)  # recursive step

# result = fac_cal(20)
# print(result)
######Chapter 6 completed###########
####Chapter 7 files reading strategy in pyhton 
# Text file and BInary files 
###Fn= open("file_name", "mode might be read or write the given file")
# WD= with open("E:\Madhav sir Paper\sbk.csv", "r") as:
# data = WD.readline()
# data2= WD.readline()
# print(data)
# print(data2)
# WD.close()


####Chapter -8 objects oriented Programming###########
##Creating the class associated obkectes in the pyhton 
###
# class Design:
#     def __init__(self, model):
#         self.model = model
#         print(self.model)

#     def __str__(self):
#         return f"Design Model: {self.model}"

# M1 = Design("Yatri")  
# print(M1) 

# #--int function in python--
# class Student:
#     def __init__(self, full_name, age, Blood_Group):
#         self.full_name = full_name
#         self.age = age
#         self.Blood_Group = Blood_Group
#         print(self.full_name)

# # Correctly passing all three arguments
# s1 = Student("Bikas", 25, "O+")
# print(s1)

# s2 = Student("Umisha", 22, "A+")
# print(s2)

# s3 = Student("John", 30, "B+")
# print(s3)

# s4 = Student("Alice", 28, "AB+")
# print(s4)

# ### another possiilbe exnapelns,
# class ShoppingCart:
    
#     def __init__(self):
#         self.items = []
#         self.total_price = 0

#     def add_item(self, item, price):
#         self.items.append(item)
#         self.total_price += price

#     def display_cart(self):
#         print("Items in Cart:", self.items)
#         print("Total Price:", self.total_price)

# ### Create a shopping cart and add items
# cart = ShoppingCart()
# cart.add_item("Laptop", 1000)
# cart.add_item("Headphones", 150)
# cart.display_cart()
###Chapter 9 lecture  parts of OOPS
# class Nepal:
#     print("Welcome to land of Himalaya")
    
#     def __init__(self, Name, age):
#         self.Name = Name
#         self.age = age

# # For printing the details value
# ID = Nepal("Bikas", 25)
# print(f"Name: {ID.Name}, Age: {ID.age}")


#####private and public attributes in pyhton
# class Account:
#     def __init__(self, account_number, account_name, balance):
#         self.__account_number = account_number
#         self.__account_name = account_name
#         self.__balance = balance
 
# ###To print the function 
# AD = Account(45783790283, "Bikas Basnet", 250000)
# print(AD)
####Inheritance concepts in pyhton: Single , Multiple and multilevel inheritance 
##here the properties of first class is inherted to the another mdoel of the drone
# # Base class
# class Drone:
#     def __init__(self, model, battery_life):
#         self.model = model
#         self.battery_life = battery_life

#     def fly(self):
#         return f"The {self.model} drone is flying for {self.battery_life} hours."

# # First-level child class
# class CameraDrone(Drone):
#     def __init__(self, model, battery_life, camera_resolution):
#         super().__init__(model, battery_life)
#         self.camera_resolution = camera_resolution

#     def capture_photo(self):
#         return f"The {self.model} camera drone is capturing a photo with {self.camera_resolution} resolution."

# # Second-level child class (grandchild of Drone)
# class RacingDrone(CameraDrone):
#     def __init__(self, model, battery_life, camera_resolution, speed):
#         super().__init__(model, battery_life, camera_resolution)
#         self.speed = speed

#     def race(self):
#         return f"The {self.model} racing drone is racing at a speed of {self.speed} km/h."

# # Creating an object of RacingDrone
# racing_drone = RacingDrone("Speedster X1", 2, "4K", 120)

# # Using methods from each class in the inheritance chain
# print(racing_drone.fly())              # The Speedster X1 drone is flying for 2 hours.
# print(racing_drone.capture_photo())     # The Speedster X1 camera drone is capturing a photo with 4K resolution.
# print(racing_drone.race())              # The Speedster X1 racing drone is racing at a speed of 120 km/h.


