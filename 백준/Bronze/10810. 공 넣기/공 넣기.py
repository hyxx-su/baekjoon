n, m = map(int, input().split())

nlist = [0 for i in range(n)]

for i in range(m):
    i, j, k = map(int, input().split())
    l = j-i
    for ii in range(l+1):
        nlist[i-1+ii] = k

print(*nlist)