mnp = input()

m = int(mnp.split()[0])
n = int(mnp.split()[1])
p = int(mnp.split()[2])

unuzece = [x for x in range(1,11)]
listanote = []
dic = {}
mediemax = 0
k = 0

for i in range(m):
    nume = input()
    note = input()
    if len(note.split()) != n:
        quit()
    dic[nume] = note
    listanote = note.split()
    for j in listanote:
        if int(j) not in unuzece:
            quit()

for x in dic:
	y = dic[x].split()
	z = [int(i) for i in y]
	medie = sum(z)/len(z)
	if mediemax < medie:
		mediemax = medie
		numestudent = x
	if medie >= 8 and p != 0:
		k = k + 1
		p = p - 1

print(k)                
print(numestudent, "%.2f" % mediemax)
