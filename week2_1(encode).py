
a = 680351 * 3262739
s = str(a)
s2 = ''
for i in s:
    k = format(i.encode('ascii')[0], 'b')
    k = '0'*(8-len(k)) + k
    s1 = "00" + k[0] + '0' + k[1:4] + '0' + k[4:]
    h0 = int(s1[2]) ^ int(s1[4]) ^ int(s1[6]) ^ int(s1[8]) ^ int(s1[10])
    h1 = int(s1[2]) ^ int(s1[5]) ^ int(s1[6]) ^ int(s1[9]) ^ int(s1[10])
    h2 = int(s1[4]) ^ int(s1[5]) ^ int(s1[6]) ^ int(s1[11])
    h3 = int(s1[8]) ^ int(s1[9]) ^ int(s1[10]) ^ int(s1[11])
    s1 = str(h0) + str(h1) + k[0] + str(h2) + k[1:4] + str(h3) + k[4:]
    s1 = ''.join(reversed(s1))
    s2 += s1
_l =[]
while len(s2) != 0:
    s1 = s2[:8]
    s2 = s2[8:]
    _l.append(int(s1, base=2))
print(_l)