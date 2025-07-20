n, m = map(int, input().split())

a = int(input())
b = (m + a) // 60
c = (m + a) % 60

n += b

if n < 23:
    print(n, c)
else:
    n = n % 24
    print(n, c)