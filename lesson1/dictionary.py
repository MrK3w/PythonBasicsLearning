my_dict = {'key1':'value1','key2':'value2'}

#print(my_dict)
#print(my_dict['key1'])

d = {1:123,2:[0,1,2],3:{'insideKey':100}}

print(d[2][2])
print(d[3]['insideKey'])

e = {'key1':['a','b','c','d']}
print(e['key1'][3].upper())