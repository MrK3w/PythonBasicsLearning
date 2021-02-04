import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        #x1,y1 = self.coor1
        return math.sqrt((self.coor1[0] - self.coor2[0]) ** 2 + (self.coor1[1] - self.coor2[1]) ** 2)
    
    def slope(self):
        # Y2 - Y1 / X2 - X1
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(f"distance is {li.distance()} and slope is {li.slope()}")

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)


c = Cylinder(2,3)