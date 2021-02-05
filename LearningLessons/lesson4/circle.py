class Circle():

    #CLAS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print(my_circle.get_circumference())