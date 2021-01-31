import math
#numbers are basic type variable can be 1.5 float or 3 int
#Strings are just some arrays of characters which builds a text
# Lists are collection of data you can add there what you want and then pop it, add or remove elemnts []
# Tuples are similar to list but cannot be modified they look ()
# dictionaries are collection which are created from key and value key is unique value and it is for searching in dictionary

#equation = 100 + 0.25 * 1

#44
#29
#34

#float
#print(4**4)
#print(math.sqrt(16)) or 100 ** 0.5

#s = 'Hello'

#print(s[1])
#print(s[::-1])
#print(s[4])
#print(s[-1])

#newList =[1,1,1]
#addedListBySolution = [0] * 3
#newerList = []
#newerList.extend([1,1,1])
#print(newerList)

#list3 = [1,2,[3,4,'hello']]
#list3[2][2] = 'goodbye'
#print(list3)

#list4 = [5,4,3,2,1]
#list4.sort()
#print(list4)

d = {'simple_key':'hello'}
d1 = {'k1':{'k2':'hello'}}
d2 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3 =  {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])

#difference between tupples and list is that tupple cannot be changed

#set has only unique values

list5 = [1,2,2,33,4,4,11,22,3,3,2]
newSet = set(list5)
print(newSet)

# false, false, false, true, false
#false