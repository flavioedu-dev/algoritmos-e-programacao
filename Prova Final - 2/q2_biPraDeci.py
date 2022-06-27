# Função que converte de binário para decimal
def binarioPraDecimal(str):

    y = list(reversed(str)) # Convertendo *str* em lista, invertendo e atribuindo a *y*

    res = 0 # Declarando a variável *res* com valor 0

    # Laço para percorrer a lista *y*
    for i in range(len(y)):

        if int(y[i]) == 1: # Verificando se o *y* posição *i* é igual a 1.
            res += 2**int(i) # *res* recebendo 2 elevado a *i*, quando *i* é 1

    print("Decimal:", res) # Imprimindo em decimal o binário de entrada(str)

# Chamando a função e passando um *input* como parâmetro
binarioPraDecimal(input("Digite um número binário: "))