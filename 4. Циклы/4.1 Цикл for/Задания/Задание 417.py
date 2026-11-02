n = int(input())
zero = 0
neg = 0
pos = 0
count = 0
for i in range(n):
    num = int(input())
    if num == 0:
        zero = zero + 1
    elif num < 0:
        neg = neg + 1
    else:
        pos = pos + num
        count = count + 1
a = pos / count
print("Нулей:", zero)
print("Отрицательных:", neg)
print(f"Среднее положительных: {a:.2f}")