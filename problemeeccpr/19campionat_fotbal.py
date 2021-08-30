k = int(input())
n = int(input())
dic = {}
dicsortat = {}

for i in range(n):
    meci = input().split()
    echipa1 = meci[0]
    echipa2 = meci[4]

    if echipa1 in dic:
        dic[echipa1][1] += int(meci[1])
        dic[echipa1][2] += int(meci[3])
    else:
        dic[echipa1] = [0, 0, 0]
        dic[echipa1][1] = int(meci[1])
        dic[echipa1][2] = int(meci[3])

    if echipa2 in dic:
        dic[echipa2][1] += int(meci[3])
        dic[echipa2][2] += int(meci[1])
    else:
        dic[echipa2] = [0, 0, 0]
        dic[echipa2][1] = int(meci[3])
        dic[echipa2][2] = int(meci[1])

    if meci[1] > meci[3]:
        dic[echipa1][0] += 3
    elif meci[1] == meci[3]:
        dic[echipa1][0] += 1
        dic[echipa2][0] += 1
    elif meci[1] < meci[3]:
        dic[echipa2][0] += 3

if len(dic) != k:
    print("Nu ati introdus suficiente echipe")
    quit()

for k,v in sorted(dic.items(), key=lambda x: x[1][0], reverse=True):
    dicsortat[k] = v
    
for i in dicsortat:
    print(i, " ".join([str(j) for j in dic[i]]))
