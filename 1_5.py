disbursement = int(input("Введите издержки"))
gain = int(input("Введите выручку"))
if disbursement > gain:
    print("Убыток фирмы :", gain - disbursement)
else:
    print("Прибыль фирмы :", gain - disbursement)
    print("Рентабельность :", ((gain - disbursement) / gain) * 100, "%")
    workers = int(input("Введите количество сотрудников"))
    print("Выручка на одного сотрудника :", (gain - disbursement) / workers)
