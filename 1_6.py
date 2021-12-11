a = int(input("Первый результат"))
b = int(input("Желаемый результат"))
counter = 1
while a < b:
    a *= 1.1
    counter += 1
print(f"На {counter} день спортсмен достиг результата - не менее {b} км")
