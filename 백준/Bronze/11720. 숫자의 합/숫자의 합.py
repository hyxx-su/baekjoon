n = int(input())
m = list(map(int, input()))
cnt = 0

for i in range(n):
    cnt += m[i]
print(cnt)