# Arbitrary KeyWord Arguments

# def mutilply(*args):
#     result=1
#     for num in args:
#         result *= num
#     return result
#
# mutilply(1,2,4,3)

# def multiply(*args):
#     result=1
#     for num in args:
#         result += num
#     return result
#
# multiply(1,3,2,7)

def decscribe_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

decscribe_person(name="abc",age="25",city="Pune")
