x = ("samsung", "iphone", "tecno", "redmi" )
print(x[0])

print(x[-2])

phones = list(x)
phones[1] = "itel"
x = tuple(phones)
print(x)

phones = list(x)
phones.append("Huawei")
x = tuple(phones)
print(x)

for phone in x:
    print(phone)

phones = list(x)
phones.pop(0)
x = tuple(phones)
print(x)

cities = tuple(("Kampala", "Jinja", "Mbarara", "Gulu", "Mbale"))
print(cities)

city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)

print(cities[1:4])

first = ("John", "Isaac", "Mary")
second = ("Arnest","Albert", "Mutebi")
joined = first + second
print(joined)

colors = ("red", "blue", "green")
print(colors * 3)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))

