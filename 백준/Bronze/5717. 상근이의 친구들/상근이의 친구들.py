nlist = []

while True:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        else:
            nlist.append(n+m)
    except:
        break

print(*nlist, sep="\n")