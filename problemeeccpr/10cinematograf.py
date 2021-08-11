orasosire = int(input().replace(":", ""))
n = int(input())
ore = []
preturi = []
numefilme = []
minim = float("inf")
indecsi = []
oredisponibile = []
preturidisponibile = []
index = 0

for i in range(n):

    datefilm = input().split()

    ora = datefilm[0].replace(":", "")
    ore.append(int(ora))

    pret = datefilm[1]
    preturi.append(int(pret))

    nume = datefilm[2]
    numefilme.append(nume)

for i in range(len(ore)):
    if ore[i] >= orasosire:
        indecsi.append(i)
        oredisponibile.append(ore[i])

for i in indecsi:
    if ore[i] <= min(oredisponibile):
        preturidisponibile.append(preturi[i])

for i in oredisponibile:
    if minim > i:
        minim = i
        index = ore.index(minim)
    elif minim == i:
        index = preturi.index(min(preturidisponibile))

print(numefilme[index])
