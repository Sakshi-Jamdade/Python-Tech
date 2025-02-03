# def f1():
#     num=int(input("Enter No : "))
#     print("\n")
#     for i in range(num+1,0,-1):
#         x="*"
#         print(x*i)
# f1()

# def f1():
#     num=int(input("Enter No : "))
#     print("\n")
#     for i in range(1,num+1):
#         x="*"
#         print(x*i)
# f1()


#Recursive_Factorial Program

def function(n):
    if n==0:
        return 1

    return n*function(n-1)

result=function(5)
print(result)

