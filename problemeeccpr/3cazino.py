n = int(input())

carti = {}
k = 0
cartefalsa = "JOC OK"

for i in range(n):                                          
    carte = input()                         #adauga n carti 
    if carte in carti:
        carti[carte] += 1                   #dictionarul va primi o cheie de tip string cu numele cartii, daca aceasta este deja in dictionar se adauga la valoarea ei +1
    else:
        carti[carte] = 1                    #daca nu, adauga cheia cu valoarea = 1

    if carti[carte] == 3 and k == 0:        #daca valoarea cheiei, referita prin variabila carte, ajunge la 3 se afiseaza cartea falsa
        cartefalsa = carte
        k = 1

print(cartefalsa)
