r = [7, 7, 6, 4, 2, 1]
a = int(input("Поставте оценку"))  # Условий про ограничение выборки не было :)
if a <= 1:
    r.append(a)
elif a > r[0]:
    r.insert(0, a)
else:
    for i in range(len(r) - 1):
        if r[i] >= a > r[i + 1]:
            r.insert(i + 1, a)
            break
print(r)
