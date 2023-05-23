thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

i = 0
while i<len(thislist):
    print(i," = ",thislist[i])
    i+=1


[print(x) for x in thislist]

count = [1,2,3,4,5]
ans = [x for x in count if x%2==0]
print ([x for x in count if x%2 == 0])

lista = [12,13]
listb = [1,2]
lista.extend(listb)
lista = [ x for x in listb]
lista = [x for x in range(10)]
listx = [x for x in range(100) if x%2 == 0]
print(listx)
print(lista)
newlist = [x for x in range(10) if x %2 == 0]
print(newlist)

fruits = ["mango","jango","python","cobra"]
nFruits = [x.upper() for x in fruits]
print(fruits)
print(nFruits)

