n = int(input())
nlist = []

for i in range(n):
    m = int(input())
    nlist.append(m)

for i in range(n-1):
    m = nlist[i]
    if m == 1:
        print("#")
    else:
        o = m-2
        print("#"*m)
        for i in range(o):
            print("#"+"J"*o+"#")
        print("#"*m)
    print()

m = nlist[-1]

if m == 1:
    print("#")
else:
    o = m-2
    print("#"*m)
    for i in range(o):
        print("#"+"J"*o+"#")
    print("#"*m)