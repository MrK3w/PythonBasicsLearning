"""
Toto je skript pro 1. cviceni.
Doplnte kod dle pokynu cviciciho.
"""

def add(a, b):
    """Adds parameters."""
    return a + b

def what_number(number):
    if number < 0:
        return 'negative'
    elif number > 0 :
        return 'positive'
    else: 
        return 'zero'

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def ship_name(fleet, designated_no):
    if designated_no in fleet.keys(): 
        return fleet[designated_no]
    else:
        return 'no fleet'

#add 1 if number in number == 5
def how_many_5(numbers):
   return sum( 1 for number in numbers if number == 5 )

def gen_list_gt(lst, no):
    return [ item for item in lst if item > no ]

def fact(n):
    if n < 0:
        return "cannot be negative"
    elif n == 1 or n == 0:
        return 1
    else: 
        return n * fact(n-1)


def dividable_by(lst, divisor):
    dividable_integer =  [x for x in lst if type(x) is int and not x % divisor] [0]
    print (f'Integer dividable by {divisor} is: {dividable_integer}')


#print(add([1, 2, 3], [4, 5, 6]))


#for example: find first number dividable by ...
lst = [8,16,24,32,64 ]
divisor = 8
dividable_by(lst, divisor)

#n = 5
#print("Number", n, "is:", what_number(n))

#lst = [1, 2, 3, 6, 7, 8]
#print("Sum is:", sum_of_numbers(lst))

#fleet = {'BS62': 'Pegasus', "BS75": "Galactica", 36: 'Valkirie'}
#designated_no = "BS62"
#print("We've got {} in the fleet".format(ship_name(fleet, designated_no)))

#function to count how many numbers > 5 are in the list
#lst = [1, 2, 5, 6, 7, 10, 12, 40, 3]
#print(f"There are {how_many_5(lst)}x number 5")

#generating list example
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#no = 5
#print(f"List with numbers > {no}: {gen_list_gt(lst, no)}")

#print(fact(-5))
