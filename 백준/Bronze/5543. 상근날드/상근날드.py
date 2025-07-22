nlist = []
mlist = []

for i in range(3):
    n = int(input())
    nlist.append(n)

for i in range(2):
    m = int(input())
    mlist.append(m)

n = min(nlist)
m = min(mlist)

print(n+m-50)