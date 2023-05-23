"""

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


"""



mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-1])

if "cherryx" in thislist:print("Yes")
else:print("No")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(1,"xx")
print(thislist)

mylist = []
mylist.insert(1,"OK")
mylist.insert(0,"Dk")
mylist.insert(0,"Kx")
mylist.insert(3,"DD")

mylist.extend(thislist)
print(mylist)

# You can add tuple inside a list !using extend() function
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#remove list item

mylist.pop(0)
mylist.remove('mango')
mylist.remove('orange')
print(mylist)

#delete list

conlist = [1,2,3]
print(conlist)
del conlist
print(conlist)

mlist = ['1','2','3']
print(mlist)
mlist.clear()
print(mlist)
