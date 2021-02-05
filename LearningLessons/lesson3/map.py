def square(num):
    return num**2


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
    
my_nums = [1,2,3,4,5]
#map will connect method and for ex. list
#(this operation will be done for every element then you need to iterate or cast to list)
newList = list(map(square,my_nums))
print(newList)

mynames = ['John','Cindy','Sarah','Kelly','Mike']

print(list(map(splicer,mynames)))
