a, b = map(int, input().split())
c, d = map(int, input().split())

n = a + d
m = b + c

if n > m:
    print(m)
else:
    print(n)