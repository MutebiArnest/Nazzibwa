# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return f"{self.name} says Woof!"

#     def get_age(self):
#         return self.age

#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             raise ValueError("Age cannot be negative.")
        
# #creating an object of the Dog class
# my_dog = Dog("Buddy", 3)
# print(my_dog.name)
# print(my_dog.get_age())

# #create object level attributes and methods
# my_dog.set_age(4)
# print(my_dog.get_age())

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        return f"{self.name} serves {self.cuisine} cuisine."

    def open_restaurant(self):
        return f"{self.name} is now open!"
restaurant = Restaurant("Pasta Palace", "Italian")
print(restaurant.name)
print(restaurant.cuisine)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

restaurant2 = Restaurant("Sushi World", "Japanese")
print(restaurant2.describe_restaurant())
restaurant3 = Restaurant("Taco Town", "Mexican")
print(restaurant3.describe_restaurant())
restaurant4 = Restaurant("Burger Barn", "American")
print(restaurant4.describe_restaurant())

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        return f"Name: {self.first_name} {self.last_name}, Email: {self.email}"

    def greet_user(self):
        return f"Hello, {self.first_name} {self.last_name}!"
    
user1 = User("John", "Doe", "john.doe@example.com")
print(user1.describe_user())
print(user1.greet_user())
user2 = User("Jane", "Smith", "jane.smith@example.com")
print(user2.describe_user())
print(user2.greet_user())
