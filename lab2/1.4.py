print("=== Задание 4: Сумма и количество чисел ===")
print("Введите целые числа (0 - для завершения):")

total_sum = 0
count = 0

while True:
    num = int(input("Число: "))
    if num == 0:
        break
    total_sum += num
    count += 1

print(f"Сумма всех чисел: {total_sum}")
print(f"Количество чисел: {count}")