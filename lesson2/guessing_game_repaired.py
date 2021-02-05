from random import randint

def startGame():
    rndNumber = randint(1,100)
    print(rndNumber)
    guessedNumbers = []
    while True:
        guessedNumbers.append(int(input("Enter a number ")))
        if validateGuess( guessedNumbers,rndNumber) != None:
            print(validateGuess(guessedNumbers,rndNumber))
        if rndNumber == guessedNumbers[-1]:
            break
    print(f"You have it and took you {len(guessedNumbers)} guesses ")

def validateGuess(guessedNumbers, rndNumber):
    if guessedNumbers[-1] < 0 or guessedNumbers[-1] > 100:
         print("OUT OF BOUNDS")
         return
    if len(guessedNumbers) == 1:
        if rndNumber < guessedNumbers[-1]+10 and rndNumber > guessedNumbers[-1] -10:
            return "WARM!"
        else:
            return "COLD!"
    if abs(rndNumber - guessedNumbers[-1]) < abs(rndNumber - guessedNumbers[-2]):
        return("WARMER!")
    else:
        return("COLDER!")


startGame()