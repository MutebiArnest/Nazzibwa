#lambda function  to sort a list of fruits by their length
fruits = ["cherry", "banana", "date", "apple", "mango"]
fruits.sort(key=lambda x: len(x))
print(fruits)

#recursive function factorial of 5
# def factorial(n):
#     if n<1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

#count down from 10 to 1
# def countdown(n):
#     if n < 1:
#         print("Countdown finished!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(10)

#fibonacci sequence in the range of 10
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

#binary search of a number in the array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
print(f"Index of {target}: {result}")