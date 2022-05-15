""" 
Faça um programa em Python em que o usuário deverá informar três valores inteiros positivos, x,
y e z. Os valores x e y, sendo x < y, formam um intervalo de valores inteiros. O valor de z deverá ser
menor ou igual a y (z <= y). O programa deverá imprimir todos os valores inteiros compreendidos
no intervalo [x, y] divisíveis por z. Após impressão, o programa deverá informar também a soma
dos valores que são pares impressos.
Exemplos:
Entradas 1: x = 5, y = 19 e z = 3;
Saída 1: 6 9 12 15 18, soma pares= 36 
"""

a = input("Digite três números inteiros positivos: ").split() # Recebendo as entradas

# Convertendo as entradas e as atribuindo à variáveis
x = int(a[0])
y = int(a[1])
z = int(a[2])

soma = 0

if(len(a)==3): # Verificando se foram adicinados as três entradas solicitadas
    
    if x<y and z<=y: # Verificando se as condições para as entradas foram atendidas

        for i in range(x, y+1): # Iniciando o intervalo apartir do valor das variáveis x e y

            if i%z==0: # Verificando se o número atual é divisível pelo valor de z

                # Verificação só para adicionar a vírgula após o último número divisível por z
                if i==(y-1) or i==(y): 
                    print(i, end=", ")

                    # Verificando se o número é par para realizar sua adição a variável "soma"
                    if i%2==0: 
                        soma += i
                else:
                    print(i, end=" ")

                    # Verificando se o número é par para realizar sua adição a variável "soma"
                    if i%2==0:
                        soma += i

        print("Soma dos pares = ", soma)
        
# Tratamento de erros
    else:
        print('''
        É necessário que o primeiro número digitado seja menor que o segundo e o terceiro menor ou igual ao segundo:
        Número 1 < Número 2
        Número 3 <= Número 2
        ''')

elif len(a)>3:
    print("Quantidade de números digitados acima do permitido")

else:
    print("Quantidade de números digitados abaixo do permitido")