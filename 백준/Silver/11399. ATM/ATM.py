n = int(input())
nlist = list(map(int, input().split()))
mlist = []

nlist.sort()

for i in range(1, n+1):
    cnt = 0
    for ii in range(i):
        cnt += nlist[ii]
    mlist.append(cnt)
    
print(sum(mlist))