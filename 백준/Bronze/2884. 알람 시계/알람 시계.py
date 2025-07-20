n, m = map(int, input().split())

if m >= 45:
    m -= 45
    print(n, m)
else:
    if n != 0:
        n -= 1
        m += 15
        print(n, m)
    elif n == 0:
        n = 23
        m += 15
        print(n, m)