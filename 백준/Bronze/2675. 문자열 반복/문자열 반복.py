n = int(input())
nlist = []
rlist = []

for i in range(n):
    r, s = input().split()
    s = list(s)
    rlist.append(r)
    nlist.append(s)

for i in range(n):
    for ii in nlist[i]:
        print(ii*int(rlist[i]), end="")
    print()