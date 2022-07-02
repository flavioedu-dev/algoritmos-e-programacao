n = int(input("Tamanho das suas matrizes: "))

matrizA = []
matrizB = []

def matrizes(n):

    for i in range(n):
        
        linha = []

        for j in range(n):
            linha.append(float(input("Digite o valor de A(%i,%i): " % (i+1,j+1))))

        matrizA.append(linha)

    for i in range(n):
        
        linha = []

        for j in range(n):
            linha.append(float(input("Digite o valor de A(%i,%i): " % (i+1,j+1))))

        matrizB.append(linha)

    print(matrizA)
    print(matrizB)

matrizes(n)