import copy

while True:
    n = int(input("Tamanho das suas matrizes: "))

    if n<=1:
        print("Tamanho da matrizes precisa ser inteiro e maior que 1!")
    else:
        
        matrizA = []
        matrizB = []

        def matrizes(n):

            for i in range(n):
                
                linha = []

                for j in range(n):
                    linha.append(int(input("Digite o valor de A(%i,%i): " % (i+1,j+1))))

                matrizA.append(linha)

            for i in range(n):
                
                linha = []

                for j in range(n):
                    linha.append(int(input("Digite o valor de B(%i,%i): " % (i+1,j+1))))

                matrizB.append(linha)

        # Matriz *B* Diagonal
        def diagonal(matB):

            matDig = copy.deepcopy(matB)

            for i in range(len(matB)):

                for j in range(len(matB)):

                    if j < i:
                        matDig[i][j] = 0

            return matDig

        # Matriz *A* Transposta
        def transposta(matA):

            matTrans = []

            for i in range(len(matA)):
                matTrans.append([])

            for i in matA:

                for j in range(len(i)):
                    matTrans[j].append(i[j])

            return matTrans

        # Matriz *B* Crescente
        def crescente(matB):

            matCresc = copy.deepcopy(matB)
            cresc = []

            for i in matB:

                for j in i:
                    cresc.append(j)

            cresc.sort()

            for i in range(len(matB)):

                for j in range(len(matB)):
                    matCresc[i][j] = cresc[0]
                    cresc.pop(0)

            return matCresc

        # Multiplicando as novas Matrizes
        def multi(diag, trans, cresc):

            digTrans = []
            matFinal = []

            for i in range(len(diag)):
                digTrans.append([])
                matFinal.append([])

            for i in range(len(diag)):

                for j in range(len(diag)):

                    total = 0

                    for k in range(len(diag)):
                        total += diag[i][k]*trans[k][j]

                    # print(total)
                    digTrans[i].append(total)

            for i in range(len(diag)):

                for j in range(len(diag)):

                    total = 0

                    for k in range(len(diag)): 
                        total += digTrans[i][k]*cresc[k][j]

                    # print(total)
                    matFinal[i].append(total)

            print("--- Matriz A ---")
            for i in matrizA:
                print(i)

            print("--- Matriz B ---")
            for i in matrizB:
                print(i)

            print("--- Plantinha Crescida! ---")
            
            for i in matFinal:
                print(i)


        matrizes(n)
        multi(diagonal(matrizB), transposta(matrizA), crescente(matrizB))

        break