a = int(input())
b = int(input())

c = a*(b-((b//10)*10))
d = a*(((b-((b//100)*100))//10))
e = a*((b//100))
f = a*b

print(c)
print(d)
print(e)
print(f)