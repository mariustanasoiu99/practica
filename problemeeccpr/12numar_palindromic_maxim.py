n = int(input())

cifre = [i for i in input().strip().split()[:n]]
cifre.sort()

index = 0
tmp = -1

for i in range(1, len(cifre)):
    if int(cifre[i]) != int(cifre[i-1]):
        if cifre.count(cifre[i]) == 1 or cifre.count(cifre[i]) == 3:
            index += 1
            if cifre.count(cifre[i]) == 3:
                tmp = i
                
if index <= 1:
    if len(cifre) % 2 == 1:
        if tmp == -1:
            sir = cifre[0]
            for i in range(1, len(cifre), 2):
                sir = cifre[i] + sir + cifre[i+1]
        else:
            sir = cifre[tmp]
            cifre.pop(tmp)
            for i in range(0, len(cifre), 2):
                sir = cifre[i] + sir + cifre[i+1]
    else:
        sir = ''
        for i in range(0, len(cifre), 2):
            sir = cifre[i] + sir + cifre[i+1]
    print(sir)
else:
    print(0)
