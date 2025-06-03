import sys

n = sys.stdin.readline().strip()
nlist = list(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline().strip()
mlist = list(map(int, sys.stdin.readline().split()))

cnt = {}

for i in nlist:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in mlist:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")