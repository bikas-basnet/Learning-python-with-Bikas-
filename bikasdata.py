# x = 5
# y = 7
# print(x+y)
# Bikas=("Bikas is the earliest molercular biologist\n from sankhuwasava Nepal")
# #to deal with the next function called input
# name=input("Enter your Name")
# print(name)
# #the input is always capture as string so to convert the data type to another form
# Roll=int(input("Enter your Roll Number"))
# print(Roll)
# #how to find the data type 
# age=int("Enter your age: ")
# print(type(age))
#To find the sum of two Number
# Number1 = int(input("Enter Number First"))
# Number2 = int(input("Enter number second"))

# sum = Number1 + Number2

# print("The the sum of the number is", sum)
#operator of the python
#+,/*- and % is used for the modulus used to calculate Remainder , // nearlest whole number ** is the Exponciation
# n1=-5
# n2=132
# divide=n1%n2
# print(divide)
# print("Sum", 4 + 3)
# print("Product", 4*3)
# print("Substraction", 4-3)
# print("Exponents", 4**3)
# print("Divison", 4558/89)
# print("Modulus", 5856995//9)
# print("Remainder", 88986%9)
#Assignement operators
# x = 10
# y = "hello"
# x = 5
# x += 3  # Equivalent to x = x + 3
# print(x)  # Output: 8
# y = 10
# y -= 2  # Equivalent to y = y - 2
# print(y)  # Output: 8
# z = 4
# z *= 2  # Equivalent to z = z * 2
# print(z)  # Output: 8
# a = 12
# a /= 3  # Equivalent to a = a / 3
# print(a)  # Output: 4.0 (float)
# b = 9
# b %= 5  # Equivalent to b = b % 5
# print(b)  # Output: 4
# c = 13
# c //= 4  # Equivalent to c = c // 4
# print(c)  # Output: 3 (integer result)
# d = 2
# d **= 3  # Equivalent to d = d ** 3
# print(d)  # Output: 8
# e = 8  # Binary: 1000
# e <<= 1  # Equivalent to e = e << 1
# print(e)  # Output: 16 (Binary: 10000)
# f = 16  # Binary: 10000
# f >>= 1  # Equivalent to f = f >> 1
# print(f)  # Output: 8 (Binary: 1000)
# g = 10  # Binary: 1010
# h = 6  # Binary: 0110
# g &= h  # Equivalent to g = g & h
# print(g)  # Output: 2 (Binary: 0010)
# g = 5  # Binary: 0101
# h = 7  # Binary: 0111
# g |= h  # Equivalent to g = g | h
# print(g)  # Output: 7 (Binary: 0111)
# g = 8  # Binary: 1000
# h = 6  # Binary: 0110
# g ^= h  # Equivalent to g = g ^ h
# print(g)  # Output: 14 (Binary: 1110)
#comaprision operators in python
# x = 5
# y = 3
# result = x == y  # False
# print(result)
# # x = 5
# y = 3
# result = x != y  # True
# x = 5
# y = 3
# result = x < y  # False
# x = 5
# y = 3
# result = x > y 
# print(result) # True
# x = 5
# y = 3
# result = x <= y  
# print(result)
##3lofical operators in python
# x = 5
# y = 10
# Z = 15
# result1 = x > 0 and y > 0
# print(result1)  # True
# result2 = x > 0 or y < 0  #if one of the operator commes to true
# print(result2)
# result3 = not(x > y)
# print(result3)
####33#identity operators in python
# x = 5
# y = 7
# print("x is equal to y", x is y)
# print("x is not equal to y", x is not y)
# ###33#memebership operators in pyhton
# Criminal = ("Miraj", "Bisal", "Rabin", "Akash")
# print("if Bikas is present in Criminal:" , "Bikas" in Criminal)
# print("Bikas is not in present in criminal", "Bikas" not in Criminal)
##3333#3Bitwise operators in python
#0 and 1 is called binary number system, and 0-9 is called decimal number
#so how can i convert to decimal number system to Binary number system
# a = 10  # Binary representation: 1010
# b = 5   # Binary representation: 0101

# # Bitwise AND
# print("Bitwise AND:", a & b)  # Output: 0 (Binary representation: 0000)

# # Bitwise OR
# print("Bitwise OR:", a | b)   # Output: 15 (Binary representation: 1111)

# # Bitwise XOR
# print("Bitwise XOR:", a ^ b)  # Output: 15 (Binary representation: 1111)

# # Bitwise NOT
# print("Bitwise NOT of a:", ~a)  # Output: -11 (Binary representation: 11110101)

# # Left Shift
# print("Left Shift of a:", a << 1)  # Output: 20 (Binary representation: 10100)

# # Right Shift
# print("Right Shift of a:", a >> 1)  # Output: 5 (Binary representation: 0101)
# x = 15
# y = 20
# print("Bitwise operator of:", x | y)
### calculate the volume of the sphere 
# # lets take an input
# radius = float(input("Enter the radius of the sphere:"))
# volume= (4/3)*3.1415* radius**3
# print("The volume of the sphere is:", volume)
##3#operating the multiple operators so which operators commes first and
#which operation perform first is associated with the BODMAS rule(Brackets oppens,
#Division, Multiplication, Addition , Substraction)

# Solve = 3 * 5 ** 8 // 2 * (5 * 5)
# # print(Solve)
# Bikas=3.9080
# print(type(Bikas))#type function indicates the deta types 
###i am going to make a tutle graphics in pyhton
# import turtle
# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")

# # Create a turtle
# t = turtle.Turtle()
# t.speed(0)  # Set the fastest drawing speed

# # Define colors
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# # Draw a colorful spiral
# for i in range(360):
#     t.pencolor(colors[i % 6])  # Cycle through colors
#     t.width(i/100 + 1)
#     t.forward(i)
#     t.left(59)

# # Hide the turtle
# t.hideturtle()

# # Keep the window open
# turtle.done()
##3# to create the flower like tutule grahics in pyhton
# from turtle import *
# import colorsys
# speed(0)
# bgcolor("black")
# h = 0
# for i in range(16):
#     for j in range(18):
#         c = colorsys.hsv_to_rgb(h, 1, 1)
#         color(c)
#         h += 0.0005
#         rt(90)
#         circle(150 - j * 6, 90)
#         lt(90)
#         circle(150 - j * 6, 90)
#         rt(180)
#     circle(40, 24)
# done()
###3333next desingn for the pythin codingof the graphics 
# from turtle import*
# import colorsys
# speed(90)
# hideturtle()
# bgcolor("black")
# tracer(5)
# width(2)
# h=0.01
# for i in range(55):
# 	color(colorsys.hsv_to_rgb(h,1,1))
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	right(120)
# 	circle(50)
# 	left(240)
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	h+=0.02
# 	color(colorsys.hsv_to_rgb(h,1,1))
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	right(120)
# 	circle(-50)
# 	left(240)
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	left(2)
# 	h+=0.02
# done()

    
    