
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# def calculate_area(length, width):
#     area = length * width
#     return area

# result = calculate_area(length, width)
# print("The area of the rectangle is:", result)

# function to display student information (name, age, course and student number)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# course = input("Enter your course: ")
# student_number = input("Enter your student number: ")

# def display_student_information(name, age, course, student_number):
#     print("Student Information:")
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)
#     print("Student Number:", student_number)

# display_student_information(name, age, course, student_number)

#create a function that calculates the area of a circle
radius = float(input("Enter the radius of the circle: "))
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

result = calculate_circle_area(radius)
print("The area of the circle is:", result)

#program demostrating betweem local and global variables
x = 10  # global variable  
def my_function():
    x = 5  # local variable
    print("Inside the function, x =", x)
my_function()
print("Outside the function, x =", x)