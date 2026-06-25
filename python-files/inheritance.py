class Animal:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_details(self):
        print(f"Animal name {self.name} it has {self.age} years old and it of {self.breed} breed ")

class Dog(Animal):
    def make_sound(self):
        print(self.name, "barks")

dog1 = Dog("bad", 4,"idegenous")
dog1.display_details()
dog1.make_sound()

class Bull(Animal,Dog):
    def print_name(self):
        print(self.name)

b = Bull("biggie",5,"local")
b.display_details
b.make_sound

#method resolution order