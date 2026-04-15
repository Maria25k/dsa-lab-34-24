m = float(input("Введите число m: "))

print(f"Последовательность (1*m, 2*m, ..., 10*m):")
for i in range(1, 11):
    print(i * m, end=" ")
print("\n")