k = int(input())
m = int(input())
n = int(input())
match k,n:
    case _,0:
        print(0)
    case 1,0:
        print(2 * n * m)
    case _,_ and if n <= k:
        print(m * 2)
    case _:
        b = (2*n + k - 1) // k
        print(b * m)
