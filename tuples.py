# my_tp=(10,20,22.23,"Sara",True,30,40)
# print(my_tp[0])
# print(my_tp[-1])                #Indexing

# print(my_tp[1:3])
# print(my_tp[:2])                #Slicing
# print(my_tp[:-1])

# print(my_tp[::-1])              #Reversing The Tuple
# print(my_tp[3:6])


# ***************** Operations On Tuple:

# ****1. Concatenation
# t1=(1,2,3,4)
# t2=(5,6)
# t3=t1+t2;
# print(result)     O/p=(1,2,3,4,5,6)
#
# t1=(1,2,3,4)
# t2=(5,6)
# result=t1+t2
# print(result)

# ****2. Repetition
# t1=(1,2)
# print(t1*3)

# ****3.Length
# t1=(1,2,3)
# print(len(t1))

# ****4.Membership
# my_tuple=(10,20,30,40)
# print(10 in my_tuple

# my_tuple=(10,20,30,40)
# result=list(my_tuple)       #Tuple2List
# print(result)
# print(type(result))
#
# a=tuple(result)             #List2Tuple
# print(a)
# print(type(a))

# UnPacking
# -You Can Extract The Values From Tuples Into Variables

# my_tuple=(10,20,30)
# a,b,c=my_tuple
# print(a,b,c)
#
# second_eg=("Sara",29,"Niya",5,69)
# a,b,c,d,e=second_eg
# print(a,b,c,d,e)

# Nested Tuple
# Tuple inside the another Tuple

# batch=(("Khushal", 102, 85),("Arav", 101, 90))
# print(batch[1][2])
#
# Limitations
# 1.Can't Modify


my_tuple=(10,50,90,40)

# print(sorted(my_tuple))
# print(reversed(my_tuple))
#
# Tuple Packing nad Unpacking
# Pack and Unpack data Dynamically
# data=("Khushal",101,83)
# name,roll,no=data
# print(f"Name Is {name} and Roll No {roll} And No {no}")
#
# data=("India","Maharashtra","Pune")
# Country,State,District=data
# print(f"Country Is {Country} and Country {Country} And District {District}")
#
# data=("1202","Sakshi","CS")
# empId,empName,empDept=data
# print(f"Employee Id {empId} Employee Name {empName} And Depertment {empDept}")

del(my_tuple)
print(my_tuple)

