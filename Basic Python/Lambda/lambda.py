x = lambda a : a + 10
print(x(5))

y = lambda p:p*5
print(y(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

print(myfunc(4))