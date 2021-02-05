class Animal():
    def __init__(self,name) -> None:
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):    
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


def pet_speak(pet_class):
    print(pet_class.speak())

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())
