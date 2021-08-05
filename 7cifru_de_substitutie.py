n = input()
m = input().split()
tabelsubs = {}
textcriptat = ""

for i in range(len(m)):
    subs = m[i].split(",")
    tabelsubs[subs[0]] = subs[1]

for i in n:
    if i in tabelsubs:
        i = tabelsubs[i]
        textcriptat += i
    else:
        i = i
        textcriptat += i
        
print(textcriptat)



