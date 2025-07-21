Aclass = {
    "Algorithm":"204",
    "DataAnalysis":"207",
    "ArtificialIntelligence":"302",
    "CyberSecurity":"B101",
    "Network":"303",
    "Startup":"501",
    "TestStrategy":"105"
}

n = int(input())
nlist = []

for i in range(n):
    m = input()
    nlist.append(Aclass[m])

print(*nlist, sep="\n")