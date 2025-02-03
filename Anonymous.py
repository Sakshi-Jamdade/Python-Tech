# Lambda Function :
# In Python, Lambda Function is A Small, Anonymous Function
# Defined Using Lambda Kayword
# Unlike Regular Function Created Using Def, Lambda Function Are Typically Used For Short, Simple Operation
# And Are Often Utilized In Situations Where A Function Is Required For A Limited Scope, Such As Within ANother Function or As An
from email.headerregistry import UniqueSingleAddressHeader

# Syntax :
# lambda paramater:expresssion

# Example :
# def add(x,y):
#     return x+y

# add_lambda = lambda x,y : x+y
#
# print(add_lambda (2,3))

# Use Case :
# In Situation Requiring Small,Throwaway Functions
# Often Used With Function Like Map(),Reduce(), Filter()


# add=lambda x,y:x+y
# result=add(5,3)
# print(result)

# square=lambda x:x*x
# result=square(4)
# print(result)

# Even=lambda x:x%2==0
# result=Even(4)
# print(result)

# max_num=lambda x,y:x if x>y else y
# result=max_num(10,11)
# print(result)

# add_lambda = lambda x,y : x-y
#
# print(add_lambda (8,3))
#
# add_lambda = lambda x,y : x*y
#
# print(add_lambda (2,3))
#
# add_lambda = lambda x,y : x/y
#
# print(add_lambda (10,2))
#
# Square_Lambda =  lambda x: x*x
# print(Square_Lambda(10))
#
# Rect_Lambda =  lambda l,b: l*b
# print(Rect_Lambda(10,5))
#
# Triangle_Lambda =  lambda l,h: l*h*0.5
# print(Triangle_Lambda(10,5))

# Using map() Function :
# numbers =[1,2,3,4,5]
# squared=list(map(lambda x:x**2, numbers))
# print(squared)

# numbers =[1,2,3,4,5]
# nums=[1,2,3,4,5]
# squared=list(map(lambda x,y:x+y, numbers,nums))
# print(squared)

# names =["Sara","KARUNA","Sakshi","SurajRaje"]
# Upper=list(map(lambda x:x.lower(), names))
# print(Upper)

# Using Filter() Function :
# It Is Same Like A Map() Function it Is Also Takes two Arguments First A Function Ans
# Second An Iterable Object And return List Object Of Only true Values

# numbers = [1,2,3,4,5]
# Even_Numbers = list(filter(lambda x: x % 2 == 0,numbers))
# print(Even_Numbers)

# numbers = [1,2,3,4,5]
# Odd_Numbers = list(filter(lambda x: x % 2 != 0,numbers))
# print(Odd_Numbers)

# names = ["Sara","KARUNA","Sakshi","SurajRaje"]
# Length = list(filter(lambda x:len(x)>4, names))
# print(Length)

# names = ["a","b","c","d","o","i"]
# # vowels=["a","e","i","o","u"]
# # Find_vowels = list(filter(lambda x: x in vowels, names))
# Find_vowels = list(filter(lambda x:'aeiou' in x,names))
# print(Find_vowels)

# names = ["Sara","KARUNA","Sakshi","SurajRaje"]
# Upper = list(filter(lambda x: x.startswith('K'), names))
# print(Upper)

# Using sorted() Function
# names = ["KARUNA","Sakshi","SurajRaje","Aarya"]
# Sorted_names = sorted(names,key=lambda x:len(x))
# print(Sorted_names)

# names = ["KARUNA","Sakshi","SurajRaje","Aarya"]
# Sorted_names = sorted(names,key=lambda x:x)
# print(Sorted_names)


names = [1,2,3,4,32,1,34,21,42,521,1211]
Sorted_names = sorted(names,key=lambda x:x)
print(Sorted_names)
