import sys

arr = [int(x) for x in sys.argv[1:]]

print("Исходный массив:", arr)
print("Пары соседних отрицательных чисел:")

for i in range(len(arr) - 1):
    if arr[i] < 0 and arr[i + 1] < 0:
        print(arr[i], arr[i + 1])

unique_arr = []

for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print("Массив без повторений:", unique_arr)