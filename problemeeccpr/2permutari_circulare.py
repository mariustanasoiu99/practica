n = int(input())

n_binar = bin(n)[2:]                                        #transforma numarul introdus intr-un numar binar de forma "0b.."(de tip string), fac slice sa scap de "0b"
n_binarlist = [int(i) for i in n_binar]                     #parcurg sirul n_binar element cu element si le adaug pe rand la o lista n_binarlist

listapermutari =[[n_binarlist[i - j] for i in range(len(n_binarlist))] for j in range(len(n_binarlist))]    #parcurg lista de n ori(n = lungimea listei) si permut la fiecare parcurgere ultimul element la primul element
                                                                                                            #la fiecare parcurgere listapermutari primeste o sublista
n_final = 0
for i in listapermutari:                                    #parcurg listapermutari
	n_binarstr = "".join([str(j) for j in i])           #transform fiecare sublista intr-un sir
	n_decimal = int(n_binarstr, 2)                      #transform fiecare sir intr-un nr decimal
	if n_decimal > n_final:
		n_final = n_decimal                         #verific care este cel mai mare nr decimal din lista           
                            
print(n_final)
