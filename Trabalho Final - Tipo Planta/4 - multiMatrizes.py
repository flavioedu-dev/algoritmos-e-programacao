a = [[2, 3],
     [0, 3]]

b = [[1, 3],
     [2, 4]]

crescente = [[2, 2],
             [3, 3]]

n = 2

digTrans = []
matFinal = []

for i in range(n):
    digTrans.append([])
    matFinal.append([])


for i in range(len(a)):

    for j in range(len(a)):

        total = 0

        for k in range(len(a)):
            total += a[i][k]*b[k][j]

        print(total)
        digTrans[i].append(total)

for i in digTrans:
    print(i)


for i in range(len(a)):

    for j in range(len(a)):

        total = 0

        for k in range(len(a)): 
            total += digTrans[i][k]*crescente[k][j]

        print(total)
        matFinal[i].append(total)

for i in matFinal:
    print(i)