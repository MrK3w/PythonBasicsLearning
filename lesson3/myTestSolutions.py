import math

def vol(rad):
    return 4/3 * math.pi * rad ** 3

def ran_check(num,low,high):
    return num in list(range(low,high+1))

def up_low(s):
    my_dict = {'upper':0,'lower':0}
    for letter in s:
        if letter[0].isupper():
            my_dict['upper'] += 1
        if letter[0].islower():
            my_dict['lower'] += 1
    return my_dict

def unique_list(lst):
   newSet = list(set(lst))
   print(newSet)

def multiply(numbers):  
    sum = numbers[len(numbers)-1]
    numbers.pop()
    while(len(numbers) != 0):
        sum *= numbers.pop()
    return sum

def palindrome(s):
    return s == s[::-1]

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def ispangram(str1):
    alphabetList = []
    str1 = str1.lower()
    for character in str1:
        if character in char_range('a','z') and character not in alphabetList:
            alphabetList.append(character)
    if len(alphabetList) == 26:
        return True 
    else:
        return False
 
print(ran_check(2,3,5))