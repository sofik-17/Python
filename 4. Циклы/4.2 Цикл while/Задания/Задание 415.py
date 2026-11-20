old_num = -float("inf")
max_len = 0
inc = 0
dec = 0
while (n := int(input())) != 0:
    if n < old_num:
        dec += 1
        inc = 1
    elif n > old_num:
        inc += 1
        dec = 1
    else:
        inc = 1
        dec = 1
    max_len = max(max_len, inc, dec)
    old_num = n
print(max_len)