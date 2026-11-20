old_num = 0
max_count = 0
count = 0
while (n := int(input())) != 0:
    if n == old_num:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count
    old_num = n
print(max_count)