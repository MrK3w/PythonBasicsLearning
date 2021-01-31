def convert_list_to_string(org_list, seperator=' '):
    return seperator.join(org_list)   

#find lesser number
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

#check if two words text starts with the same letter
def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]

#Is sum of this two numbers bigger or equal to 20? If yes return true
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

#Make M and D upper sign
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

#reverse sentence
def master_yoda(text):
    return ' '.join(text.split()[::-1])

#Given an integer n, return True if n is within 10 of either 100 or 200 
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
     for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True  
     return False

# Given a string, return a string where for every character in the original 
# there are three characters
def paper_doll(text):
    newSentence = ''
    for char in text:
        newSentence += char *3
    return newSentence

# Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum 
# by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    myCards = [a,b,c]
    total = sum(myCards)
    if total <= 21:
        return total
    elif 11 in myCards:
        total -=11
        if total <= 21:
            return total
    return 'BUST'


def spy_game(nums):
    numbers = ""
    for number in nums:
        numbers += str(number)
    if '007'  in numbers: 
        return True
    return False

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')