from os import system, name 
gameBoard = []

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def printGameBoard(listOfSigns):
    clear()

    i = 0
    j = 0
    print("#|0|1|2|")
    print('-' * 8)
    while(i < 3):
        print(f"{i}|",end = "")
        while(j < 3):
            print(listOfSigns[i][j],end = "|")
            j += 1
        print('\n' + '-' * 8)
        i += 1
        j = 0
    
def getInput():
    while True:
        try:
            position = int(input("Please enter your position 0-2: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return position

def UserInput():
    while True:
        positions = []
        positions.append(getInput())
        positions.append(getInput())
        
        if IsPositionValid(positions): 
            break 
        else:
            print("Bad position")
    return positions

def IsBoardFull():
    for oneList in gameBoard:
        if ' ' in oneList:
            return False
    else:
        print("It's a draw!")
        return True

def CheckLine():
    i = 0
    j = 0
    while j < 3:
        line = []
        while i < 3:
            line.append(gameBoard[i][j])
            i += 1
        if len(set(line)) == 1 and ' ' not in line:
            return True
        j += 1
        i = 0
    return False


def CheckDiagonal():
    firstCross = [gameBoard[0][0],gameBoard[1][1], gameBoard[2][2]]
    secondCross = [gameBoard[0][2],gameBoard[1][1], gameBoard[2][0]]
    if (len(set(firstCross)) == 1 and ' ' not in firstCross) or (len(set(secondCross)) == 1 and ' ' not in secondCross):
        return True
    return False

def CheckRow():
    for boardLine in gameBoard:
        if len(set(boardLine)) == 1 and ' ' not in boardLine:
            return True

def IsItWin(playerOne):
    if CheckRow() or CheckLine() or CheckDiagonal():
        if playerOne:
            print('x win')
            return True
        else:
            print('o win')
            return True
    return False


def IsPositionValid(positions):
    #if position it's out of game boards returns false
    if (positions[0] < 0 or positions[0] > 2) or (positions[1] < 0 or positions[1] > 2):
        return False
    #if this cell is not empty then return false
    elif (gameBoard[positions[0]][positions[1]] != ' '):
        return False
    else:
        return True

def PlayGame():
    #list of game plan
    global gameBoard
    gameBoard =  [[" "," "," "],[" "," "," "],[" "," "," "]]
    question = "Player do you want to play like x or o?"
    #player one(X)
    while True:
        playerChoice = input(question).lower()
        if playerChoice == 'x':
            playerOne = True
            break
        elif playerChoice == 'o':
            playerOne = False
            break
    clear()
    print("TIC TAC TOE GAME STARTS!")

    #Game is running till one player wins or game board is full and then it's a draw
    while True:
        positions = UserInput()
        #put sign on cell selected by user if player one is true than it's a X otherwise O
        if playerOne:
            gameBoard[positions[0]][positions[1]] = 'x'
        else: 
            gameBoard[positions[0]][positions[1]] = 'o'
        
        #switch players
        printGameBoard(gameBoard) 
        if(IsItWin(playerOne)):
            break
        playerOne = not playerOne

        if IsBoardFull():
            break
    usersAnswer = (input("Do you want to play again? Y/N: ")).upper()
    if usersAnswer == 'Y':
        PlayGame()
    else:
        print("Thanks for playing!")

PlayGame()





