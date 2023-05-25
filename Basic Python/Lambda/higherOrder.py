myItem = [3,5,7,9]
def cubeFunction(func,itemList):
    result = []
    for x in itemList:
        result.append(func(x))
    return result

power = 3
cubeResult = cubeFunction(lambda x:x**power,myItem)
print(cubeResult)