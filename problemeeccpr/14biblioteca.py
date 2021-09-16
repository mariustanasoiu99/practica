lin = input().split()
D = int(lin[0])
k = int(lin[1])

i = 0
n = []
p = []

while i < k:
    lin = input().split()
    n.append(int(lin[0]))
    p.append(int(lin[1]))
    i += 1

m = []
while sum(n)>0:
    i = 0
    copieD = D
    raft = []
    while i < k:
        if n[i] != 0 and p[i] <= copieD:
            raft.append(p[i])
            copieD -= p[i]
            n[i] -= 1
        else:
            i += 1
    m.append(raft)

for Raft in m:
    print(" ".join([str(i) for i in Raft]))
