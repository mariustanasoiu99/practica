n = int(input())
biti = input()
secvente = []
index_anterior = 0
dic = {}

for i in range(len(biti)):
    if biti[i] == '0':
        secvente.append(biti[index_anterior:i])
        index_anterior = i
secvente.append(biti[index_anterior:len(biti)])

for i in range(len(secvente)):
    secvente[i] = secvente[i].replace('0', "")

for i in secvente:
    if i != "":
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

temp = 1
ok = 1
for i in range(len(dic)):
    temp2 = temp * 10 + 1
    if str(temp) not in dic:
        dic[str(temp)] = 0
    if str(temp) in dic and str(temp2) in dic:
        if  dic[str(temp)] < dic[str(temp2)]:
            ok = 0
            break
    temp = temp2
temp = 1
for i in range(len(dic)):
    print(dic[str(temp)], end=' ')
    temp = temp * 10 + 1
print("")
print(ok)
