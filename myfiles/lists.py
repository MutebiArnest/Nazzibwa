names = [ "Alice", "Brian", "Charles", "Diana", "Eric"]
print(names[1])

names[0] = "Andrew"
print(names)

names.append("Faith")
print(names)

names.insert(2, "Bathel")
print(names)

names.pop(3)
print(names)

print(names[-1])

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Lemon"]
print(fruits[2:5])

countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print(countries_copy)

for country in countries:
    print(country)

animals = ["zebra", "lion", "antelope", "elephant", "cat"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

for animal in animals:
    if "a" in animal:
        print(animal)

first_names = ["John", "Mary"]
second_names = ["Doe", "Jane"]

full_list = first_names + second_names
print(full_list)