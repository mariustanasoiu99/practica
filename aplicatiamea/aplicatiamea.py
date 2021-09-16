import lib.siruri.siruri as s
import lib.liste as l
import lib.dictionare as d

sir1 = "Aplicatia mea"
sir2 = " cu module"

s.lungime(sir1)
s.parcurgere(sir1)
s.feliere(sir1)
s.majuscule(sir1)
s.minuscule(sir1)
s.transformaresirinlista(sir1)
s.concatenare(sir1, sir2)
s.inlocuire(sir1, "Aplicatia mea", "My app")

list1 = ["primul", "al doilea", "al treilea"]
list2 = ["first", "second", "third"]

l.elementecua(list1)
l.addelementlista(list1, "al patrulea")
l.removeelementlista(list1, "al patrulea")
l.concatenarelista(list1, list2)
l.transformarelistainsir(list1)

dictionar1 = {"brand": "Dacia",
              "model": 1310,
              "an": 2000}
dictionar2 = {}

d.afisareelemente(dictionar1)
d.addelementdictionar(dictionar2, "nume", "Luke")
d.removeelementdictionar(dictionar1, "model")
