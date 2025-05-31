n = input()
abclist = "abcdefghijklmnopqrstuvwxyz"

for i in abclist:
    if i in n:
        print(n.index(i), end=" ")
    else:
        print(-1, end=" ")