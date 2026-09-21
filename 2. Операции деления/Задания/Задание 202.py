n = int(input())
time = 9 * 60
time += (n-1) * 45
a = n // 2
b = (n-1) // 2
time += a*5 + b*15
time += 45
print(time // 60, time % 60)