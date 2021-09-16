def lungime(sir):
    print(len(sir))

def parcurgere(sir):
    for x in sir:
        print(x)

def feliere(sir):
    x = sir[1:-1]
    print(x)

def majuscule(sir):
    x = sir.upper()
    print(x)

def minuscule(sir):
    x = sir.lower()
    print(x)

def transformaresirinlista(sir):
    x = sir.split(" ")
    print(x)

def concatenare(sir1, sir2):
    x = sir1 + sir2
    print(x)

def inlocuire(sir, holder, replacer):
    x = sir.replace(holder, replacer)
    print(x)
