# Continue Statement :
# In programming Continue Is Like Saying "Skip the Turn,But Keep Going With The Loop"
# Used To Skip The Iteration From The Loop And Move To Next Iteration.
# Unlike Break it Doesn't Terminate the Loop Entirely- It Just SKips The rest Of The Code For The Current Iteration
from math import factorial

# for i in range(1,10):
#     if i==5:    # Stop The Loop When i Is 5
#         continue
#     print(i)


# for num in range(10):
#     if num % 2 == 0:    # Stop The Loop When i Is 5
#         continue
#     print(num)

# i=0
# while i < 10:
#     i += 1
#     if i % 2 ==0:
#         continue
# print(i)


# balance=1000
# while True:
#     print("\n 1. Deposite")
#     print(" 2. WithDraw")
#     print(" 3. Exit")
#     choice=int(input("Enter Ur Choice : "))
#
#     if choice ==1:
#         amt=float(input("Enter Deposite Amount : "))
#         balance += amt
#         print(f"New Balance : {balance}")
#
#     elif choice ==2 :
#         amt=float(input("Enter Withdraw Amount : "))
#         if amt <= balance:
#             balance -= amt
#             print(f"New Balance : {balance}")
#         else:
#             print("InSufficient Balance")
#     elif choice ==3:
#         print("Exiting....")
#         break
#     else:
#         print("Invalid Choice...Try Again")

# Fibonaccie Series:

# n=int(input("Enter The Number Of Fibonaccie Series : "))
# a, b=0, 1
# print("Fibonaccie Sequence : ")
# for _ in range(n):
#     print(a,end=" ")
#     a,b = b,a+b

# n=int(input("Enter The Number Of Factorial : "))
# fact= 1
# while n>0:
#     fact *= n
#     n -= 1
# print(fact)

secret_number=7
while True:
    guess=int(input("Guess The Secret Number (Between 1 And 10")))
    if guess==secret_number:
        print("Congrts")
        break;
    elif guess < secret 
