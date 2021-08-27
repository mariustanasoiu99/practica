n = int(input())
temperaturi = [int(i) for i in input().split()]
nrmax = []
nrmaxfinal = []
lungimemax = float("-inf")
valpoz = 0
valneg = 0

if len(temperaturi) != n:
    print("Nu ati introdus", n, "temperaturi")
    quit()

for i in range(len(temperaturi)):
    if (temperaturi[i] >= 0 and temperaturi[i-1] < 0) or (temperaturi[i] < 0 and temperaturi[i-1] >= 0):
        nrmax.append(temperaturi[i])
    else:
        nrmaxfinal.append(nrmax)
        nrmax = []
        nrmax.append(temperaturi[i])

if nrmax not in  nrmaxfinal:
    nrmaxfinal.append(nrmax)

for i in nrmaxfinal:
    if lungimemax <= len(i):
        lungimemax = len(i)
        secventa = i
        
for i in temperaturi:
    if i >= 0:
        valpoz += 1
    else:
        valneg += 1

if valpoz == 0 or valneg == 0:
    print(0)
else:
    raportpoz = valpoz*100/len(temperaturi)
    raportneg = valneg*100/len(temperaturi)
    print(lungimemax)
    print(" ".join(str(i) for i in secventa))
    print("+:{:.2f}%".format(raportpoz), "-:{:.2f}%".format(raportneg))
