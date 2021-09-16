import lib.siruri.siruri as s

s.inlocuire("test", "test", "succes")

def afisareelemente(dictionar):
    for chei, valori in dictionar.items():
        print(chei, ": ", valori)

def addelementdictionar(dictionar, key, value):
    dictionar.update({key: value})
    print(dictionar)

def removeelementdictionar(dictionar, key):
    dictionar.pop(key)
    print(dictionar)

