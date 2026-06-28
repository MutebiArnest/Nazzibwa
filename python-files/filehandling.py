#opening file student.txt
# with open("student.txt", "r") as file:
#     #reading the content of the file
#     content = file.read()
#     print(content)

# #without using with statement
# file = open("student.txt", "r")
# content = file.read()
# print(content)
# file.close()

# #writing to a file report.txt
# with open("report.txt", "w") as file:
#     file.write("This is a report.\n")
#     file.write("Report generated successfully.\n")

#appending i love python to report.txt
with open("report.txt", "a") as file:
    file.write("I love Python!\n")
