n, x = map(int, input().split())
nlist = list(map(int, input().split()))

for i in range(n):
    if x > nlist[i]:
        print(nlist[i], end=" ")