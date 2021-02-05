def ask():
    while True:
        try: 
            x = int(input("Enter a number: "))
        except ValueError: 
            print("Wrong input")
            continue
        else: 
            break
    print(x**2)


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("There was a type error!")

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("All done")

ask()