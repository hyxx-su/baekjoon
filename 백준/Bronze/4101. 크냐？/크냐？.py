a = True
nlist = []

while a:
    n, m = map(int, input().split())
    
    if n+m == 0:
        a = False
    elif n > m:
        nlist.append("Yes")
    else:
        nlist.append("No")

print(*nlist, sep="\n")