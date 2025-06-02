n = int(input())
m = int(input())
cnt = 0

ablist = []

for i in range(m):
    a, b = map(int, input().split())
    ablist.append(a*b)

for i in ablist:
    cnt += i

if cnt == n:
    print("Yes")
else:
    print("No")