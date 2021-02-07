class Person(object):
    
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
    
    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def __str__(self):
        return " ".join((self.firstname, self.surname))

class Student(Person):
    next_id = 0
    
    def __init__(self, firstname, surname):
        Person.__init__(self, firstname, surname)
        Student.next_id += 1
        self.edison_id = Student.next_id

    def get_id(self):
        return self.edison_id

s1 = Student("Sean", "Connery")
print("ID:", s1.get_id(), "Student name:", s1)
# ID: 1 Student name: Sean Connery
print(s1.get_firstname(), s1.get_surname()) # Sean Connery
s2 = Student("James", "Bond")
print("ID:", s2.get_id(), "Student name:", s2)
# ID: 2 Student name: James Bond