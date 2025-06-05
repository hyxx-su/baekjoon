nlist = []

while True:
    try:
        n = input()
        nlist.append(n)
    except EOFError:
        break
print(*nlist, sep="\n")