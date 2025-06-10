a, b, c = map(int, input().split())
nlist = [0 for i in range(a+b+c+1)]

for i in range(1, a+1):
    for ii in range(1, b+1):
        for iii in range(1, c+1):
            nlist[i+ii+iii] += 1

print(nlist.index(max(nlist)))