class Dog():

    def __init__(self,breed,name,spots,age):
        self.breed = breed
        self.name = name
        self.spots = spots
        self.age = age

my_dog = Dog('Huskie', 'Alex',False,8)

print(my_dog.breed + " is and his name is: " + my_dog.name + f" and he is {my_dog.age} years old ")