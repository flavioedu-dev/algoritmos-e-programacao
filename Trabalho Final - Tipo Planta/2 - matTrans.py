matA = [[1,2],
        [3,4]]

matTrans = []

for i in range(len(matA)):
    matTrans.append([])

for i in matA:

    for j in range(len(i)):
        matTrans[j].append(i[j])

for i in matA:
    print(i)

print("-------------------Transposta-------------------")

for i in matTrans:
    print(i)