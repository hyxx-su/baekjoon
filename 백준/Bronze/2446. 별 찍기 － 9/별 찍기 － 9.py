n = int(input())

for i in range(1, n):
    for ii in range(i-1):
        print(" ", end="")
    for iii in range(n-i+1):
        print("*", end="")
    for v in range(n-i):
        print("*", end="")
    print()
for i in range(1, n+1):
    for ii in range(n-i):
        print(" ", end="")
    for iii in range(i):
        print("*", end="")
    for v in range(i-1):
        print("*", end="")
    print()
    