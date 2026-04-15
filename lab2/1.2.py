x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

print("Числа в интервале [1, 50]:")
for num in (x, y, z):
    if 1 <= num <= 50:
        print(num, end=" ")
print("\n")