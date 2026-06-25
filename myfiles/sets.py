beverages = set(("Tea", "Coffee", "Juice"))
print(beverages)

beverages.update(["Soda", "Water"])
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

mySet.remove("kettle")
print(mySet)

for item in mySet:
    print(item)

set1 = {"pen", "book", "desk", "chair"}
list1 = ["bag", "table"]
set1.update(list1)
print(set1)

ages = {20, 21, 22}
names = {"John", "Mary"}
combined = ages.union(names)
print(combined)