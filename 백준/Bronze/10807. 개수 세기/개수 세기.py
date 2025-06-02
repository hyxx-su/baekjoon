n = int(input())
m = list(map(int, input().split()))
o = int(input())

cnt = 0

for i in m:
    if i == o:
        cnt += 1

print(cnt)