def exp(m, n):
    return m ** n

def divides(m, n):
    i = 1
    while i <= m:
        if i % n == 0:
            print(i)
        i += 1

def is_in_string(string, c):
    return c in string

def how_many(string, c):
    total = 0
    for oneChar in string:
        if c == oneChar:
            total += 1
    return total

print(exp(2, 3)) # 8
divides(12, 3) # 3 6 9 12
divides(10, 7) # 7
print(is_in_string('Ostrava', 'x')) # True
print(how_many('Ostrava', 'a')) # 2
print(how_many('Ostrava', 'q')) # 0