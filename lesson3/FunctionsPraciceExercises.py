#find lesser number
def lesser_of_two_evens(a,b):
    if a < b:
        return a
    else:
        return b

#check if two words text starts with the same letter
def animal_crackers(text):
    words = text.split()
    if words[0][0] == words[1][0]:
        return True
    return False

#Is sum of this two numbers bigger or equal to 20? If yes return true
def makes_twenty(n1,n2):
    if n1+n2 >= 20:
        return True
    return False

def old_macdonald(name):
  newName = ''
  i = 0
  for x in name:
    if i == 0 or i == 3:
        newName += x.capitalize()
    else:
        newName += x
    i +=1
  return newName

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
        
print(old_macdonald('macdonald'))