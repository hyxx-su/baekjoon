n = str(int(input())/5)
m = 0

if n[-1] != "0":
    m = 1

print(int(n[:-2])+m)