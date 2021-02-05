class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    
    #OPERATIONS/ACTIONS ---> Methods
    def bark(self):
        print(f"WOOF! my name is {self.name}")

my_dog = Dog('Lab', 'Sam')
my_dog.bark()
print(my_dog.breed + " is his breed and his name is: " + my_dog.name)