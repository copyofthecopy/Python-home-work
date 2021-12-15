str_one = input()
crutch = str_one.split()
for i in range(len(crutch)):
    print(f'{i + 1})', crutch[i][:10])