""" Faça um programa em Python que leia um gabarito de uma prova com 10 questões, onde cada possui como resposta uma das alternativas: A, B, C, D ou E. Após ler o gabarito, o programa irá pedir o nome de um aluno e suas respostas dessa prova (cartão-resposta). Cada questão correta, o aluno soma pontos, de acordo com a tabela de pontuação a seguir:

Para cada questão errada, o aluno não soma pontos. O programa deverá informar o nome do aluno e a quantidade de pontos obtida na prova. """

# Entradas
x = input("Digite o gabarito de uma prova de dez questões(A, B, C, D, E): ").split()
y = input("Digite o nome do aluno: ")
z = input("Digite suas respostas: ").split()

entradas = ["A", "B", "C", "D", "E"]

# Verificando se foram inseridos 10 respostas
if len(x) == 10 and len(z)==10:

    cont = 0

    # Verificando se todos as respostas estão em caixa alta
    for i in range(len(x)):
        if (x[i] == x[i].upper()) and (z[i] == z[i].upper()):
            cont += 1
            continue
        else:
            print("Todas as letras precisam ser maiúsculas!")
            break

    if cont == 10:
        nota = 0

        for i in range(4):
            if x[i] == z[i]:
                nota += 15

        for i in range(4,7):
            if x[i] == z[i]:
                nota += 20

        for i in range(7,10):
            if x[i] == z[i]:
                nota += 30

        print("Aluno: %s, nota: %i" % (y, nota))

else:
    print("O gabarito do professor e do aluno precisam ter 10 respostas!")