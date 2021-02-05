mySet = set()

mySet.add(1)
mySet.add(2)
#wouldn't be added because set accept only unique values
mySet.add(1)

print(mySet)
myList = [1,1,1,1,1,1,2,2,2,2,3,3,3,4]
myNewSet = set(myList)

print(myNewSet)