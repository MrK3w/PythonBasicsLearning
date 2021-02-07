class Battlestar(object):

    def __init__(self, name, commander): # constructor
        self.name = name # instance variable
        self.commander = commander

    def identify(self): # method
        return 'This is Battlestar {0}, \commanded by {1}.'.format(self.name, self.commander)

galactica = Battlestar('Galactica', 'Bill Adama')
pegasus = Battlestar('Pegasus', 'Helena Cain')
print(galactica.identify())
# This is Battlestar Galactica, commanded by Bill Adama.
print(pegasus.identify())
# This is Battlestar Pegasus, commanded by Helena Cain.

