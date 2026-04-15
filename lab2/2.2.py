s = input("Введите строку: ")

new_s = ""
count = 0

for ch in s:
    if ch == ':':
        new_s += '%'
        count += 1
    else:
        new_s += ch

print("Результат:", new_s)
print("Количество замен:", count)