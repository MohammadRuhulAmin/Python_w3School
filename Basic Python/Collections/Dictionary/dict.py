thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "code":123
}
print(thisdict["brand"])

print(thisdict)
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict.get("year"))
print(thisdict.get("model"))
print(thisdict.keys())

thisdict['electric'] = True

print(thisdict)
print(thisdict.values())
print(thisdict.items())

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "bodel" in thisdict:print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:print("NO key value found!")

#updating item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#remove item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

for x in thisdict.values():print(x)
for x in thisdict.keys():print(x)
for x,y in thisdict.items():print(x," => ",y)

# copy dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)