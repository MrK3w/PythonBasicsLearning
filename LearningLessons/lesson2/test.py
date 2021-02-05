def startWithS(sentence):
   lst = [x for x in sentence.split() if x[0] == 's']
   print(lst)

def listOfNumbers():
    lst = [x for x in range(1,51) if x % 3 == 0]
    print(lst, end= " ")

def evenString(sentence):
   for x in sentence.split():
        if len(x) % 2 == 0:
            print(x+ " even!")

def fizBuzz():
    for x in range(1,101):
        if(x % 5 == 0 and x % 3 == 0):
            print('FizzBuzz')
        elif(x % 3 == 0):
            print('Fizz')
        elif(x % 5 == 0):
            print('Buzz')
        else:
             print (x)

def newWord(sentence):
 lst = [x[0] for x in sentence.split()]
 print(lst)



#startWithS('Print only the words that start with s in this sentence')
#print(list(range(0,11,2)))
#listOfNumbers()
evenString('Print every word in this sentence that has an even number of letters')
#fizBuzz()
st = 'Create a list of the first letters of every word in this string'
#newWord(st)