class Vector(object):
    def __init__(self, vec):
    #warning: vec will be tuple, immutable
        self.vec = vec
    
    def __add__(self, other):
        vec = []
        for no, item in enumerate(self.vec):
            vec.append(item + other.vec[no])
        return Vector(tuple(vec))

def __str__(self):
#content = ", ".join([str(i) for i in self.vec])
#return "({})".format(content)
    return str(self.vec)

v1 = Vector((1, 2, 3, 4))
print(v1)
v2 = Vector((5, 6, 7, 8))
print(v2)
v3 = v1 + v2
print(v3)