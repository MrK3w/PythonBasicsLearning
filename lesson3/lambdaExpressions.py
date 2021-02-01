square = lambda num: num **2
print(square(2))

num = lambda a,b: a+b
print(num(3,4))

my_nums = [0,1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda num: num ** 2, my_nums)))

word = "Hello"

letter = lambda word: word[0].lower()
print(letter(word))




