def exp(m, n):
    return m ** n

def divides(m, n):
    print("\ndivides: ", end= " ")
    for i in range(1,m+1):
        if i % n == 0:
            print(i, end= " ")

def is_in_string(string, c):
    return c in string

def how_many(string, c):
    total = 0
    for oneChar in string:
        if c == oneChar:
            total += 1
    return total

print(f"exponent number is: {exp(3,4)}") # 8
divides(12, 3) # 3 6 9 12
divides(10, 7) # 7
word = 'Ostrava'
letter = 'a'
print("")
print(f"Is {letter} in {word}: {is_in_string(word, letter)}") # True
print(f"How many times is {letter} in {word}: {how_many(word, letter)}") # 2
