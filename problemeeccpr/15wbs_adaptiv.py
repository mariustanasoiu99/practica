N = int(input())
n = int(input())
cod = ""

for i in range(N):
    bit = input()
    cod = cod + bit

codlist = [cod[i:i+n] for i in range(0, len(cod), n)]
codlist0 = codlist.copy()
codlist1 = codlist.copy()
codbloc = " ".join(codlist)

for i in range(len(codlist0)):
    if codlist0[i].count("0") == len(codlist0[i]) and len(codlist0[i]) > 1:
        codlist0[i] = "0"
    else:
        codlist0[i] = "1" + codlist0[i]

codlist0.insert(0, "0")
codbloc0 = "".join(codlist0)

for i in range(len(codlist1)):
    if codlist1[i].count("1") == len(codlist1[i]) and len(codlist1[i]) > 1:
        codlist1[i] = "1"
    else:
        codlist1[i] = "0" + codlist1[i]

codlist1.insert(0, "1")
codbloc1 = "".join(codlist1)

raportcompresie0 = N / len(codbloc0)
raportcompresie1 = N / len(codbloc1)

if raportcompresie0 > raportcompresie1:
    print(round(raportcompresie0, 2))
    for i in codbloc0:
        print(i)
else:
    print(round(raportcompresie1, 2))
    for i in codbloc1:
        print(i)
