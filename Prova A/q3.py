# OBS:
    # Aqui tem comentários detalhados sobre cada parte do código escrito
    # Os comentários sempre estão acima ou ao lado direito dos códigos a qual se referem
    # Talvez seja difícil entender


ent1 = input("Número de alunos e provas: ").split() # Recebendo número de alunos e provas. Ex: 2 2
pesos = input("Pesos: ").split() # Recebendo pesos. Ex: 5 8 

x = int(ent1[0]) # Recebe o número de alunos. Ex: 2
y = int(ent1[1]) # Recebe o número de provas. Ex: 2
z = [] # Criando lista vazia 'z'

for i in range(x): # De 0 a valor de 'x'. Ex: (0 a 1)
    # Recebendo as notas dos alunos. Ex:
    # Aluno 1: 2.9  9.5
    # Aluno 2: 3.0 7.0
    z.append(input("Notas aluno %i: " % (i+1)).split()) # z = [['2.9', '9.5'],['3.0' ,'7.0']]

soma = 0 # Criando a variável soma
res = [] # Criando lista vazia 'res'

# Percorrendo todos os elementos da lista 'z' (os elementos que nesse caso são listas).
# Nesse caso são dois elementos em forma de lista pois z = [['2.9', '9.5'],['3.0' ,'7.0']]
for i in z: # Primeiro o laço passará pelo elemento ['2.9', '9.5'] e depois o ['3.0' ,'7.0']

    # Usando o tamanho do elemento 'i' (no caso, a lista 'i') para percorrer cada elemento dentro do dele(porque nesse caso temos 'i' como lista)
    # len(i) = 2, pois o primeiro i é igual a ['2.9', '9.5'] e depois a ['3.0' ,'7.0']
    # Assim no primeiro 'i' percorreremos o elemento '2.9' e depois o '9.5' e no segundo '3.0' e em seguida '7.0'
    for c in range(len(i)): 

         # Convertendo cada elemento dentro de 'i' de string para float ['2.9', '9.5'] --> [2.9, 9.5]
         # i[c(quando c==0)]('2.9') -->i[c(quando c==0 após a conversão)](2.9)
         # i[c(quando c==1)]('9.5') -->i[c(quando c==0 após a conversão)](9.5)
        i[c] = float(i[c]) 

        # Convertendo cada elemento dentro de 'pesos' de string para float
        # Usamos aqui pois a quantidade de pesos é igual a quantidade de notas individuais(ou seja, igual a 'i')
        pesos[c] = float(pesos[c])

        # Multiplicando os elementos de 'i' pelos pesos
        # (Quando c==0) 2.9*5 == 14.5 // (Quando c==1) 9.5*8 == 76
        i[c] = i[c]*pesos[c]

        # Ao fim da primeira rodada desse laço ocorreu isso: 
        # z[0] = ['2.9', '9.5'] --> z[0] = [14.5, 76]
        # Ao fim da segunda rodada desse laço ocorreu isso: 
        # z[1] = ['3.0' ,'7.0'] --> z[1] = [15, 56]

    # Percorrendo todos os elementos de 'i' ('i' que está em 'z')
    for j in i:

        # Primeiro i = [14.5, 76] // Segundo i = [15, 56], então 'i' tem tamanho 2
        soma += j
        # Para o primeiro 'i':
            # Primeira vez que o laço rodou 'soma'(0) = 0 + 14.5
            # Segunda vez que o laço rodou 'soma'(14.5) = 14.5 + 76
            # 'soma' = 90.5
        # Para o segundo 'i':
            # Primeira vez que o laço rodou 'soma'(0) = 0 + 15
            # Segunda vez que o laço rodou 'soma'(15) = 15 + 56
            # 'soma' = 71

    # Primeiro 'res' recebeceu a primeira soma(90.5), então 'res' = [90.5]
    # Segundo 'res' recebeceu a segunda soma(71), então 'res' = [90.5, 71]
    res.append(soma)

    # Zerando a soma a cada vez que ela for adicionada a lista 'res', para que não aja conflito de valores 
    soma = 0 

tPesos = 0 # Criando váriável pesos

for i in pesos: # Percorrendo todos os elementos da lista pesos
    tPesos += i # 'tPesos' está recebendo a soma de todos os elemento da lista pesos, então 'tPesos' == (5+8)13


mediaAlunos = [] # Criando lista para receber a média dos alunos

# Percorrendo todo os elementos da lista 'res' // 'res' = [90.5, 71]
for i in res:

    # Adicionando a lista ''mediaAlunos' cada elemento da lista 'res' dividido por 'tPesos'. 
    # Ex: No primeiro i(i=90.5), então 'mediaAlunos' está recebendo 6.96153846 ( 90.5(i) / 13(tPesos) )
    mediaAlunos.append(i/tPesos) 

# Formatando e imprimindo as saídas
for i in mediaAlunos:
    print("%.2f" % i, end=" ")
print("(médias dos alunos)")

mediaClasse = 0 # Criando a váriavel para receber a média da classe

# Percorrendo a lista 'mediaAlunos'
for i in mediaAlunos:
    mediaClasse += i # 'mediaClasse' está recebendo a soma de todos os elemento de 'mediaAlunos'

# 'mediaClasse' recebendo ele mesmo dividido pela quantidade de médias de alunos
# Nesse caso, 'mediaClasse' = (6,96(média aluno 1) + 5,46(média aluno 2)) / 2(quantidade de médias dos alunos)
mediaClasse = mediaClasse/len(mediaAlunos) 

print("%.2f (média da classe)" % mediaClasse) # Formatando e imprimindo a média da classe