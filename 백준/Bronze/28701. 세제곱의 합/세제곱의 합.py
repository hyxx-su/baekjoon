n = int(input())
cnt = 0
cnt2 = 0

for i in range(1, n+1):
    cnt += i
    cnt2 += i**3

print(cnt)
print(cnt**2)
print(cnt2)