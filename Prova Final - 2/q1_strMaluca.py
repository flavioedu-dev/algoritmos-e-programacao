import random # Importando a biblioteca random

x = input("Digite uma frase: ") # Recebendo uma string

# Função que vai criar as strings malucas
def stringMaluca(str):    

    y = [*str] # Transformando a *str* em lista e copiando para a váriavel *z*

    # Laço para colocar os caracteres em caixa alta e baixa
    for i in range(len(y)):

        z = random.randint(0, len(x)-1) # Escolhendo um número aleatório e atribuindo para *z*

        l = random.randint(0, len(x)-1) # Escolhendo um número aleatório e atribuindo para *l*

        y[z] = y[z].upper() # Colocando em caixa alta o o caractere de *y* que está na posição *z*

        y[l] = y[l].lower() # Colocando em caixa baixa o o caractere de *y* que está na posição *z*


    k = "".join(y) # Transformando o *y* em string e atribuindo a *k*

    print(k) # Imprimando a saída *k* que é a StringMaluca

# Chamando a função e passando o *x* como parâmetro
stringMaluca(x) 
stringMaluca(x)