tpl = ('name','game','meem')
print(tpl)
print(tpl[0])
print(len(tpl))
print(type(tpl))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
if "banana" in thistuple:print("OK")
else :print("Not Ok")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#inorder to append a data inside tuple first convert it to list then insert data then convert into tuple

x = list(x)
x.append("kola")
x = tuple(x)
print(x)

#adding tuple to tuple

px = ('code','range')
py = ('mk',)
px+=py
print(px)

#to remove a tuple first you have to convert it to list

del py
