a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c

print("Минимальное число:", min_num)
print()
