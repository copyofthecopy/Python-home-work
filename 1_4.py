num = int(input())
bigger = 0
while num != 0:
    if num % 10 > bigger:
        bigger = num % 10
    num //= 10
print(bigger)