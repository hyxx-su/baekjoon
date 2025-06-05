nlist = []
cntlist = []
aeiou = "aeiou"

while True:
    try:
        n = input().lower()
        if n == "#":
            break
        else:
            nlist.append(n)
    except:
        break

for i in range(len(nlist)):
    cnt = 0
    for ii in nlist[i]:
        if ii in aeiou:
            cnt += 1
    cntlist.append(cnt)
    
print(*cntlist, sep="\n")