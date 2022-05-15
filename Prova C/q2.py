""" Faça um programa em Python que leia um gabarito de uma prova com 10 questões, onde cada possui como resposta uma das alternativas: A, B, C, D ou E. Após ler o gabarito, o programa irá pedir o nome de um aluno e suas respostas dessa prova (cartão-resposta). Cada questão correta, o aluno soma pontos, de acordo com a tabela de pontuação a seguir:

Para cada questão errada, o aluno não soma pontos. O programa deverá informar o nome do aluno e a quantidade de pontos obtida na prova. """

# Entradas
x = input("Digite o gabarito de uma prova de dez questões(A, B, C, D, E): ").split()
y = input("Digite o nome do aluno: ")
z = input("Digite suas respostas: ").split()

entradas = ["A", "B", "C", "D", "E"] # Lista com as entradas permitidas para x e z

# Verificando se foram inseridas dez respostas nas entradas de gabaritos
if len(x) == 10 and len(z)==10:

    cont = 0

    # Gerando intervalo para verificar se as entradas inseridas estão dentro das permitidas
    for i in range(len(x)):

        # Tratando o erro para caso a entrada inserida não seja permitida
        try:
            e1 = entradas.index(x[i])
            e2 = entradas.index(z[i])
            cont += 1 # Incrementando o contador
            continue
        except:
            e1 = -1
            e2 = -1
            print("Erro! Lembre-se que as únicas entradas aceitas são: A, B, C, D, E.") 
            break

    if cont == 10: # Usando o contador para verificar se as dez entradas foram permitidas

        nota = 0

        # Usando intervalos para a adição de pontos de acordo com a posição de cada resposta
        for i in range(4):
            if x[i] == z[i]:
                nota += 15

        for i in range(4,7):
            if x[i] == z[i]:
                nota += 20

        for i in range(7,10):
            if x[i] == z[i]:
                nota += 30

        print("Aluno: %s, nota: %i" % (y, nota)) # Imprimindo o resultado

else:
    print("O gabarito do professor e do aluno precisam ter 10 respostas!")