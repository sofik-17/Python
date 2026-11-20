max_num1 = -float("inf")
max_num2 = -float("inf")
while (n := int(input())) != 0:
    if n > max_num1:
        max_num2 = max_num1
        max_num1 = n
    elif n > max_num2:
        max_num2 = n
print(max_num2)
