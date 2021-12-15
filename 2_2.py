list_one = []
a = list_one.append(input("Введите первый элемент списка"))
while True:
    a = input("Добавте элемент, введите 'STOP' для завершения списка")
    if a == "STOP":
        break
    list_one.append(a)
crutch = ""
for i in range(0, len(list_one) - 1, 2):
    crutch = list_one[i]
    list_one[i] = list_one[i + 1]
    list_one[i + 1] = crutch
print(*list_one)