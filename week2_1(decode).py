
_l = [185, 107, 19, 21, 33, 146, 129, 7, 241, 66, 166, 32, 30, 16, 33, 196, 170, 75, 142, 177, 42, 82, 160, 46, 198, 228, \
      230, 102, 37, 226, 230, 140, 106, 146, 128, 43, 182, 160, 58, 242, 145]
#_l.reverse()
s = ''
for i in _l:
    s = s + '0'*(8 - len(format(i, 'b'))) + format(i, 'b')
#s = ''.join(reversed(s))
s1 = s[:12]
s1 = ''.join(reversed(s1))
s = s[12:]
a =''
while len(s) != 0:
    index = 0
    h0 = int(s1[2]) ^ int(s1[4]) ^ int(s1[6]) ^ int(s1[8]) ^ int(s1[10])
    h1 = int(s1[2]) ^ int(s1[5]) ^ int(s1[6]) ^ int(s1[9]) ^ int(s1[10])
    h2 = int(s1[4]) ^ int(s1[5]) ^ int(s1[6]) ^ int(s1[11])
    h3 = int(s1[8]) ^ int(s1[9]) ^ int(s1[10]) ^ int(s1[11])
    if h0 != int(s1[0]):
        index += 1
    if h1 != int(s1[1]):
        index += 2
    if h2 != int(s1[3]):
        index += 4
    if h3 != int(s1[7]):
        index += 8
    if int(s1[index-1]) == 0 and index != 0:
        s1 = s1[:index-1] + '1' + s1[index:]
    elif index != 0:
        s1 = s1[:index-1] + '0' + s1[index:]
    s2 = s1[2] + s1[4:7] + s1[8:12]
    a += chr(int(s2, base=2))
    s1 = s[:12]
    s1 = ''.join(reversed(s1))
    s = s[12:]
print(a)