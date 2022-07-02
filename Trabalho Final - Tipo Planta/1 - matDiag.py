matB = [[2,3],
        [2,3]]

for i in matB:
    print(i)

for i in range(len(matB)):

    for j in range(len(matB)):

        if j < i:
            matB[i][j] = 0

print("-------------------Diagonal-------------------")

for i in matB:
    print(i)