n = int(input())
m = list(map(int, input().split()))

cnt = 0

for i in range(len(m)):
    if m[i] - n < 0:
        cnt += m[i]
    else:
        cnt += n

print(cnt)