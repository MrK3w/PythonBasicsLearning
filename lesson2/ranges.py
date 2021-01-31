#list range will start on zero and continue until hit  11
newList = list(range(0,11))

print(newList)

#the same but will be stepping by two elements
list(range(0,11,2))

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
print(list(zip(mylist1,mylist2)))

# check if x is in that list (returns true) 'x' in ['x','y','z']
