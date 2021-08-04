n = int(input())
lotmax = 0
k = 0

for i in range(n):

    nrcomponente = int(input())

    if nrcomponente > 0:
        componente = input()
   
        continut = [x for x in componente.split()]

        if continut.count("C") >= continut.count("T") and continut.count("R") >= continut.count("C") and continut.count("C") >= 1 and continut.count("R") >= 1 and continut.count("T") >= 1:
            k = k + 1

        if lotmax < len(continut):
            lotmax = len(continut)

print(k, lotmax)
