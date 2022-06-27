print("Crie sua matriz! (Linhas x Colunas)")

x = int(input("Digite o número de linhas: ")) # Recebendo número de linhas e atrubuindo a *x*
y = int(input("Digite o número de colunas: ")) # Recebendo número de colunas e atrubuindo a *x*

mat = [] # Declarando o variável *mat* e atribuindo a ela uma lista vazia

# Laço para percorrer as linhas
for i in range(y):

    linha = [] # Declarando a variável *linha* e atribuindo a ela uma lista vazia

    # Laço para percorrer as colunas
    for j in range(x):
        z = float(input("Digite o número (%i,%i): " % (i+1,j+1))) # Recebendo as entradas para cada posição da matriz

        linha.append(z) # Adicionando a variável *a* a lista *linha*

    mat.append(linha) # Adicionando a lista *linha* à lista *mat*, assim formando a matriz

# Laço para imprimir a matriz linha por linha
for i in mat:
    print(i) # Imprimindo cada linha da matriz

print("Matriz criada com sucesso!")

z = float(input("Digite o escalar: ")) # Recebendo o escalar e atribuindo a variável *z*

# Função que múltiplica cada item da matriz pelo valor do escalar
def escalarMatriz(list, float):

    # Laço para percorrer cada item da lista *list*
    for i in list:

        # Laço para percorrer cada item do *i* dentro de *list*
        for j in range(len(i)):
            i[j] = i[j]*float # Multiplicando cada item do *i* pelo valor do *float*

    print("Nova matriz gerada:")

    # Laço para imprimir a matriz linha por linha, após ser multiplicada pelo escalar
    for i in list:
        print(i) # Imprimindo cada linha da matriz

# Chamando a função e passando *mat* e *z* como parâmetros
escalarMatriz(mat, z)