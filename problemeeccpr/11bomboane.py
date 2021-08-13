n = int(input())
bani = input().split()
banizicurenta = 0
gradfericire = 0
arome = []

def compara(aroma, arome):
    for i in arome:
        if aroma >= i:
            return True
        else:
            return False
        
for i in range(n):
    banizicurenta += int(bani[i])
    bomboana = input().split()
    cost_bomboana = int(bomboana[0])
    aroma_bomboana = int(bomboana[1]) 

    if cost_bomboana <= banizicurenta:
        banizicurenta = banizicurenta - cost_bomboana
        gradfericire += aroma_bomboana
        arome.append(aroma_bomboana)

    elif len(arome) == 0:
        gradfericire = gradfericire - aroma_bomboana
        
    elif compara(aroma_bomboana, arome) == True:
        gradfericire = gradfericire - aroma_bomboana

print(gradfericire)
