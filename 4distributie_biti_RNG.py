n = int(input())

nbiti = input()

if len(nbiti) != n:
    print("Nu ati introdus", n,"biti!!!")
    exit()

listabiti = []
#adaug elementele din sirul nbiti 2 cate 2 in listabiti
for i in range(0, len(nbiti), 2):
    k = nbiti[i:i+2]
    listabiti.append(k)

nrmax = 0
nrmin = 999999
#aflu maximul si minimul de aparitii al unei perechi de biti in lista
for i in listabiti:
    nr = listabiti.count(i)
    if nr > nrmax:
        nrmax = nr
    if nr < nrmin:
        nrmin = nr

r1 = nrmax/nrmin
   
nrzero = 0
nrunu = 0
#aflu nr de aparitii al lui 0 sau 1
for x in nbiti:
    if x == '0':
        nrzero = nrzero + 1
    elif x == '1':
        nrunu = nrunu +1
#verific care nr de aparitii este mai mare si fac raportul
if nrzero > nrunu:
    r2 = nrzero/nrunu
else:
    r2 = nrunu/nrzero
#afisez rapoartele cu 2 zecimale
print("{:.2f}".format(r1), "{:.2f}".format(r2))

if r1 > 1.1 or r2 > 1.1:
    print(0)
else:
    print(1)
