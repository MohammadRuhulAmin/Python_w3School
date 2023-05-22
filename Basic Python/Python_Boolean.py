print(10 == 10)
print(10>9)
print(10<9)

myvariable = ''
mylist = []
print(bool('Hello'))
print(bool(10))

#JOSS jinish!!
print(bool(myvariable)) #return false cz no value set
print(bool(mylist)) #return false cz no value set
print("##############")
print(bool(True))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("#############")
#Python also has many built-in functions that return a boolean value, like the isinstance() function,
# which can be used to determine if an object is of a certain data type:
print(isinstance("Ruhul",str))
print(isinstance(123,int))
print(isinstance(12.22,float))