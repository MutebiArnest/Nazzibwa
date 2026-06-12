data = {
    "x":1,
    "y":2
}
# print(data)

score = dict([("math", 90), ("english", 85), ("science", 95)])
# print(score["math"])
# print(score["english"])
# print(score["science"])


#removing an item
# del score["science"]
# print(score)

#using pop method
# math_score = score.pop("math")
# print(math_score)
# print(score)

#iterating through a dictionary
for key in score:
    print(key, score[key])

#nested dictionaries
students = dict([
    ("student1", {"name": "Alice", "age": 20}),
    ("student2", {"name": "Bob", "age": 22}),
    ("student3", {"name": "Charlie", "age": 21})
])
for key, student_info in students.items():
    print(f"{key}: Name: {student_info['name']}, Age: {student_info['age']}")
    