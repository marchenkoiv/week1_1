
j1 = 975
j2 = 904
a = []
for i in range(j1):
    a.append([0]*j2)
for i in range(j1):
    a[i][0] = 1
for i in range(j2):
    a[0][i] = 1
for i in range(1, j1):
    for k in range(1, j2):
        a[i][k] = a[i-1][k]+a[i-1][k-1]+a[i][k-1]
print(a[j1-1][j2-1])

#сложность алгоритма - О(M*N)