n = int(input())
cnt = 1

for i in range(n, 0, -1):
    cnt *= i

print(cnt)