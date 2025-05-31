n = 0
m = 0

for i in range(1, 10):
    a = int(input())
    if a > n:
        n = a
        m = i
        
print(n, m, sep="\n")