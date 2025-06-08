nlist = []

cnt = 0

while cnt < 100:
    try:
        n = input()
        nlist.append(n)
    except:
        break

print(*nlist, sep="\n")