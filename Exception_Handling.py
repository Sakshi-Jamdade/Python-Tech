# Error And Exception Handling

# Introduction To Error Handling:
# Definition :
#
# Error :
#     A Programming Issue That Halts Execution(e.g. Syntax Or Runtime Error)
# Exception :
#     UnExpected Events Disrupting Normal Programs Flow(e.g. Divisible By Zero)

# Why Handle Error:
#     1.Avoid Program Crashes
#     2.Enhance User Experiance
#     3.Ensure Resource Cleanup

# Types Of Errors
# Syntax Error : detected During Compilation Or Interpretation
# Runtime Error : Occurs During Execution(e.g. ZeroDivisionError)
# Logical Error : Produce Incorrect O/p Without Crashing The Program

# Demonstration Of types Of Errors :
# Syntax Error:
# print("Hello")

# Runtime Error :
# print(10/0)
#
# Logical Error :


# 2.Basis of Exception handling

#     1.Core Construct :
#         - try :Code Block To Test The Error
#         - except :Block To handle The Exception
#         - else :Executes if No Exception Occurs
#         - Finally :Executes regardless Of Exceptions (Used To CleanUp)

#     2.Advantages :
#         - Prevent Crashes
#         - Improve debugging With Specific Error Msg