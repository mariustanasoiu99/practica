n = int(input())
valori = []

primulzar = input()
primulzar = primulzar.split()
primulzarint = [int(i) for i in primulzar]                                                #creaza o lista de integers cu valorile primului zar

for x in primulzarint:
        if x not in range(1,7):
            print("Ati introdus un numar care nu se afla pe fata unui zar")
            exit()                                                                        #daca o valoare introdusa nu apartine intervalului [1;6] programul se opreste
            
if len(primulzarint) != 5:
        print("Nu ati introdus 5 valori")
        exit()                                                                            #verifica daca au fost introduse 5 numere

valori.append(primulzarint)

for x in range(n-1):                                                                          
    valoarezar = input()                   
    valoarezar = valoarezar.split()                                                     
    valoarezarint = [int(i) for i in valoarezar]                                          #creaza o lista de integers cu valorile zarului
                                                                                                    
    for y in valoarezarint:
        if y not in range(1,7):
            print("Ati introdus un numar care nu se afla pe fata unui zar")
            exit()                                                                        #daca o valoare introdusa nu apartine intervalului [1;6] programul se opreste

    if len(valoarezarint) != 4:
            print("Nu ati introdus 4 valori")
            exit()                                                                        #verifica daca au fost introduse 4 numere
            
    valori.append(valoarezarint)                                                          #lista valori primeste valorile introduse, este de tip nested list                                                
            
listsumafeteviz = []

for x in valori:
    feteviz = sum(x)
    listsumafeteviz.append(feteviz)                                                       #parcurg lista valori si fac suma fiecarei subliste
sumafeteviz = sum(listsumafeteviz)

sumatotala = (1+2+3+4+5+6) * n
sumafeteinviz = sumatotala - sumafeteviz
print(sumafeteinviz)
