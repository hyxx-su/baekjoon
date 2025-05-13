n = int(input())

for i in range(1, n+1):
    for ii in range(i):
        print("*", end="")
    for iii in range(2*(n-i)):
        print(" ", end="")
    for v in range(i):
        print("*", end="")
    print()
for i in range(1, n):
    for ii in range(n-i):
        print("*", end="")
    for iii in range(2*i):
        print(" ", end="")
    for v in range(n-i):
        print("*", end="")
    print()