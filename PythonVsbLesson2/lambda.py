sqr = lambda x: x**2
sqr(2) #4
sqr(5) #25
pow = lambda number, exponent: number**exponent
pow(2, 3) #8

map(lambda x: x**2, [2, 3, 4]) #[4, 9, 16]

mapka = map(lambda x: x, ["ahoj", "svete"])
print(list(mapka))