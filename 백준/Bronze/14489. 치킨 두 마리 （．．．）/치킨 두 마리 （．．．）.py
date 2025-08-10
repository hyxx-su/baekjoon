n, m = map(int, input().split())
i = int(input())

if i * 2 <= n + m:
    print((n + m) - i * 2)
else:
    print(n + m)