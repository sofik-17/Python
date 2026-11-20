max_num = -float("inf")
first = 0
last = 0
a = 0
while (n := int(input())) != 0:
    a += 1
    if n > max_num:
        max_num = n
        first = a
        last = a
    elif n == max_num:
        last = a
print(first, last)