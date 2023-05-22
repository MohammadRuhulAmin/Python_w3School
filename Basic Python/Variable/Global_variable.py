x = "ruhul"

def print_name():
    print("My Name is : " + x)


print_name()

#Global Key

def global_key():
    global surname
    surname = "Ruhul Amin"
    print("Calling from Global : "+ surname)

def local_key():
    print("Calling from local : " +surname)

global_key()
local_key()



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)