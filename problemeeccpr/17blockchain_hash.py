nk = input().split()
nr = int(nk[0])
k = int(nk[1])
numere = input().split()
sume = []

if len(numere) != nr:
  print("Nu ati introdus", nr,"numere")
  quit()

for n in numere:
    suma = 0
    numar = ''
    for y in range(k):
        for z in range(len(n)):
            if z == len(n)-1:
                n = numar
                if numar != '':
                    suma += int(numar)
                numar = ''
            try:
                if int(n[z]) >= int(n[z+1]):
                    numar = numar + str(int(n[z]) - int(n[z+1]))
                elif int(n[z]) <= int(n[z+1]):
                    numar = numar + str(int(n[z+1]) - int(n[z]))
            except:
                continue

    sume.append(int(suma))

print(max(sume))
