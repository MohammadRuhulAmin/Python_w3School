#packing tuple
px = ('ab','cd','ef')

#unpacking tuple
(green,yellow,red) = px
print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#Assign the rest of the values as a list called "red":
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)