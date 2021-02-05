class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        #super().__init__()
        Animal.__init__(self)
        print("DOG CREATED")

    def who_am_i(self):
        print("I am a dog")

my_animal = Animal()
my_animal.who_am_i()
my_dog = Dog()
my_dog.who_am_i()