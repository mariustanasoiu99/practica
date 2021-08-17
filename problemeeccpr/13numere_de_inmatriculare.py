nr_introduse = []

string1 = ['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS',
'CL', 'CJ','CT', 'CV', 'DB', 'DJ', 'GL', 'GR', 'GJ', 'HR', 'HD', 'IL','IS', 'IF','MM', 'MH', 'MS', 'NT', 'OT', 'PH',
'SM', 'SJ', 'SB', 'SV', 'TR', 'TM', 'TL', 'VS', 'VL', 'VN']

while True:
    n = input()
    if n == '':
        break
    nr_introduse.append(n)

for i in nr_introduse:
    if i.split()[0] in string1:
        if i.split()[1].isdigit() and len(i.split()[1]) in [2, 3]:
            if i.split()[2].isupper() and len(i.split()[2]) == 3 and i.split()[2].isalpha():
                print(i)
