n = int(input())
mlist = []
sumlist = []
sum = 0
cnt = 0

for i in range(n):
    m = input()
    mlist.append(m)

for i in range(len(mlist)):
    sum = 0
    cnt = 0
    for ii in mlist[i]:
        if ii == "O":
            cnt += 1
        else:
            cnt = 0
        sum += cnt
    sumlist.append(sum)

print(*sumlist, sep="\n")