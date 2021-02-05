from random import randint

def startGame():
    rndNumber = randint(1,100)
    numberOfTries = 0
    lastNumber = 0
    print(rndNumber)
    while True:
        guessedNumber = int(input("Enter a number "))
        numberOfTries +=1
        print(validateGuess(guessedNumber, numberOfTries, rndNumber, lastNumber))
        if rndNumber == guessedNumber:
            break
        lastNumber = guessedNumber
    print(f"You have it and took you {numberOfTries} guesses")

def validateGuess(guessedNumber,numberOfTries, rndNumber, lastNumber):
    if guessedNumber < 0 or guessedNumber > 100:
         print("OUT OF BOUNDS")
         return
    if numberOfTries == 1:
        if rndNumber < guessedNumber+10 and rndNumber > guessedNumber -10:
            return "WARM!"
        else:
            return "COLD!"
    if abs(rndNumber - guessedNumber) < abs(rndNumber - lastNumber):
        return("WARMER!")
    else:
        return("COLDER!")





startGame()