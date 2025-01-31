# Funtions And Parameters
# Parameters allows You To

# def greet_with_name(name):
#     print(f"Hello, {name} ! Welcome To The Stancy Batch ")
#
# greet_with_name("Sara")
# greet_with_name("Sakshi")
# greet_with_name("Niya")

# Functions To calculate Square Of The Numbers
# The Return Function Allows a Function to send a result back to caller.
# Use Cases : Calculations, Transformation etc.

# def square(number):
#     return number*number
# result=square(8)
# print(result)

# def Sum_Of_Numbers(a,b):
#     return a+b
# print(Sum_Of_Numbers(28,34))


# def Area_Of_Rect(l,b):
#     return l*b
# print(Area_Of_Rect(28,34))

# l=int(input("Enter Length : "))
# b=int(input("Enter Breadth : "))
# def Area_Of_Rect(l,b):
#     return l*b
# print(Area_Of_Rect(l,b))

# h=int(input("Enter Height : "))
# b=int(input("Enter Breadth : "))
# def Area_Of_Triangle(h,b):
#     return 0.5*h*b
# print(Area_Of_Triangle(h,b))

# r=int(input("Enter Radius : "))
# def Area_Of_Circle(r):
#     return 3.14*r*r
# print(Area_Of_Circle(r))

# r=str(input("Enter String : "))
# def Reverse_String(r):
#     return r[::-1]
# print(Reverse_String(r))

r=int(input("Enter Number : "))
def Odd_Even(r):
    if r%2==0:
        return "Even"
    return "Odd"

print(Odd_Even(r))