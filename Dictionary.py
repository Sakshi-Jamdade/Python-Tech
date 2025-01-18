# Dictionary :

# Collection of key-values pair
# Each Must be 1.Unique 2.Immutable 3.and Acts As an identifier for the corresponding value

# Syntax :
#Creating A Dictionary
from optparse import Values

student = {
    "name" : "Sakshi",
    "Age" : 20,
    "Grade" : "O"
}

student = {
    "name" : ["q","w","r","e"],
    "Age" : [10,20,12,18],
    "Grade" : ["O","A+","A","O+"]
}

# Accesing Values

print(student.keys())
print(student.values())
print(student.get("age"))
print(student.items())
print(student)
