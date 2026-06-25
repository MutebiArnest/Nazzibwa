class Person:
    def __init__(self, name, ID_number):
        self.name = name
        self.ID_number = ID_number

    def display_info(self):
        print(f"Name: {self.name}, ID Number: {self.ID_number}")

class Student(Person):
    def __init__(self, name, ID_number, course):
        super().__init__(name, ID_number)
        self.course = course #course is a major of the student

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, ID_number, department):
        super().__init__(name, ID_number)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

student1 = Student("John Doe", "S12345", "Computer Science")
lecturer1 = Lecturer("Dr. Smith", "L67890", "Mathematics")  

student1.display_info()
lecturer1.display_info()