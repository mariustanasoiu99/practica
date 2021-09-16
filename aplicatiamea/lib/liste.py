import lib.siruri.siruri as s

s.parcurgere("test")

def elementecua(lista):
    listanoua = [i for i in lista if "a" in i]
    print(listanoua)

def addelementlista(lista, element):
    lista.append(element)
    print(lista)

def removeelementlista(lista, element):
    lista.remove(element)
    print(lista)

def concatenarelista(lista1, lista2):
    lista3 = lista1 + lista2
    print(lista3)

def transformarelistainsir(lista):
    x = "".join(lista)
    print(x)

