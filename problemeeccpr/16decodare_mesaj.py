n = input()
mesaj = []
i = 0
dic = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
       6: 'F', 7: 'G', 8: 'H', 9: 'I',
       10: 'J', 11: 'K', 12: 'L',
       13: 'M', 14: 'N', 15: 'O',
       16: 'P', 17: 'Q', 18: 'R',
       19: 'S', 20: 'T', 21: 'U',
       22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

while i <= len(n):
    try:
        if n[i] + n[i+1] != '00':
            if int(n[i] + n[i+1]) < 27:
                nr = int(n[i] + n[i+1])
                if nr in dic:
                    mesaj.append(dic[nr])
                    i += 2
            else:
                nr = int(n[i])
                mesaj.append(dic[nr])
                i += 1
        else:
            mesaj.append(" ")
            i += 2
    except:
        break
    if i == len(n)-1:
        mesaj.append(dic[int(n[i])])
        
print("".join(mesaj))
