""" Faça um programa que leia n valores inteiros positivos do usuário. O programa deverá informar se a sequência de valores digitada está em ordem crescente ou não.

Exemplos:

Entradas 1: n = 5, 6 9 12 17 18
Saída 1: Está em ordem crescente!

Entradas 2: n = 11, 1 3 5 8 9 13 11 12 20 34 99
Saída 2: Não está em ordem crescente! """

# Entrada
n = input("Digite a quantidade de valores a serem lidos e após a vírgula os valores: ").split(",")

# Convertendo e atribuindo as entradas as variáveis
x = int(n[0])
y = n[1].split()
z = []

# Verificando se a quantidade de entradas inseridas é igual a quantidade definida
if x == len(y):

    # Convertendo e adicionando os itens lista "y" para a lista "z"
    for i in range(x):
        z.append(int(y[i]))

    # Criando uma nova lista em "a" e a colocando em ordem crescente
    a = [*z]
    a.sort()

    # Comparando "z" com "a" e assim verificando e "z" está em ordem crescente
    if z == a:
        print("Está em ordem crescente!")

    else:
        print("Não está em ordem crescente!")

# Tratando o erro, caso a quantidade de entradas inseridas seja diferente da quantidade definida
else:
    print("A quantidade de entradas inseridas deve ser igual a quantidade definida!")