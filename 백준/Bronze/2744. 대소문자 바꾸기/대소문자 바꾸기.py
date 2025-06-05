n = list(input())
nlist = []

for i in n:
    if i.isupper():
        nlist.append(i.lower())
    else:
        nlist.append(i.upper())

print(*nlist, sep="")