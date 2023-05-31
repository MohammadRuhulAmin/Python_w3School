class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


obj = Person("Ruhul",28)
print(obj.name)

class Animal:
    def __init__(self,animalName,type,age):
        self.animalName = animalName
        self.type = type
        self.age = age

    def printInfo(self):
        text = "The Animal Name is {}.And it is {} type Animal and its about {} years old"
        print(text.format(self.animalName,self.type,self.age))


a1 = Animal("Lion","Ferocious",4)
print(a1.printInfo())

# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.

class Veachel:pass
class Modern:pass
class Fish:pass

class People:
    def __init__(self,name,email,contact):
        self.name = name
        self.email = email
        self.contact = contact


p1 = People("Ruhul","r@gmail.com","1023")
print(p1.name)
print(p1.email)
print(p1.contact)