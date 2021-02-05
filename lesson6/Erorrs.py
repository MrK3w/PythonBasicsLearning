def add(n1,n2):
    print(n1+n2)

result = 0
try:
    result = 10 + "HOHO"
except: 
    print("hey it looks like you aren't adding correctly")
else:
    print("Add went well!")
    print(result)

