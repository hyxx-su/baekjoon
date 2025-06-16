n = int(input())
nlist = []
for i in range(n):
    mlist = list(input())
    m = len(mlist)
    j = "no"

    if m >= 6 and m <= 9:
        j = "yes"
    
    nlist.append(j)

print(*nlist, sep="\n")