k = int(input())
m = int(input())
n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(2 * n * m)
elif n <= k:
    print(2 * m)
else:
    b = (2*n + k - 1) // k
    print(b * m)
