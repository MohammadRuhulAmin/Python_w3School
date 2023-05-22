
str = "   Hello, String "
print(str.upper())
print(str.lower())
#function work from left to right!
print(str.strip().upper().lower())
print(str.strip().lower().upper())
print(str.replace('H','J'))
print(str.split(','))