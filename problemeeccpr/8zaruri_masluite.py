n = int(input())

fetezar = [x for x in range(1,7)]
listanumere = []
 
for i in range(n):
    numere = int(input())
    if numere in fetezar:
        listanumere.append(numere)

maxim = float('-inf')
minim = float('inf')

for i in listanumere:
    aparitii = listanumere.count(i)
    if maxim < aparitii:
        maxim = aparitii
    if minim > aparitii:
        minim = aparitii
        
if minim == maxim:
    minim = 0
    
if maxim - minim > (10/100)*n:
    print(1)
else:
    print(0)
