matB = [[2,3],
        [2,3]]

matCres = []

for i in matB:

    for j in i:
        matCres.append(j)

matCres.sort()

for i in range(len(matB)):

    for j in range(len(matB)):
        matB[i][j] = matCres[0]
        matCres.pop(0)

print("-------------------Crescente-------------------")

for i in matB:
    print(i)