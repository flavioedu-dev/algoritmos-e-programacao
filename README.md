# Algoritmos e Programação
Repositório para realizar atividades e exercícios em python.
- Prova Final - Tipo 2
- Trabalho Final - Tipo Planta

---------------------------------------------------------------------------------------
## Prova Final

#### 1) String Maluca! Num programa em Python, crie uma função que receba uma string e transforma alguns dos caracteres em maiúsculos e outros em minúsculos. Defina de forma aleatória para escolher os índices dos caracteres que serão alterados. 

<b>Exemplo:</b>
<br><br>
<b>Entrada 1:</b> Linguagem de Programação<br>
<b>Saída 1:</b> LingUagEM dE proGRAmaÇãO
<br><br>
<b>Entrada 2:</b> Linguagem de Programação<br>
<b>Saída 2:</b> LiNGuAgeM de pRogRamAçÃO


#### 2) Defina as seguintes funções em Python com os seguintes protótipos:

- <b>int</b> binarioPraDecimal( <b>str</b> ): uma função que recebe um valor string, sendo esta uma cadeia de caracteres com 0 ou 1, representando um valor em binário, e converte para decimal, devolvendo como um valor inteiro;

- <b>list</b> escalarMatriz( <b>list</b>, <b>float</b> ): uma função que recebe uma matriz como lista e um valor real, o qual será o escalar a multiplicar cada elemento dessa matriz. A função devolve a matriz calculada pelo escalar como uma lista.
<br>
Crie um ou dois algoritmos em Python que utilize estas funções definidas.


## Trabalho Final - Tipo Planta
<b>Minha equipe:</b>
- Flávio Eduardo de Moura
- Ruan Lauro Cardoso da Silva Monteiro
- Marcos Vinícius Santo de Deus Ramos


### Problema 
Sabendo-se que <b>Anxn</b> e <b>Bnxn</b> são as matrizes quadradas de ordem <b>n</b> lidas por seu programa, considere a seguinte expressão matemática dada por <b>Rnxn</b>:

<b>Rnxn= Bnxn TS ∗ Anxn T ∗ Bnxn OC</b><br>

onde:

<b>Bnxn TS:</b> matriz triangular superior de Bnxn. Numa matriz triangular superior todos os elementos que
se encontram abaixo da diagonal principal são zeros;<br>
<b>Anxn T:</b> matriz transposta da matriz Anxn;<br>
<b>Bnxn OC:</b> matriz Bnxn com todos seus valores ordenados em ordem crescente.<br>

Faça um programa em Python que leia a dimensão n (n > 1) que valerá para as matrizes A e B. Em seguida leia valores inteiros para ambas as matrizes. O seu programa deverá calcular e imprimir a <b>matriz resultante R</b>, cuja expressão matemática já foi apresentada.

Exemplos de casos de testes:

<b>Caso 1:</b><br>
n = 3<br>
<b>Matriz A:</b><br>
1 2 3<br>
4 5 6<br>
7 8 9<br>
<b>Matriz B:</b><br>
9 8 7<br>
6 5 4<br>
3 2 1<br>
<b>Saída:</b><br>
1848 2202 2556<br>
750 897 1044<br>
90 108 126<br>

<table>
<tr>
<td>
<b>Caso 1:</b><br>
n = 3<br>
<b>Matriz A:</b><br>
1 2 3<br>
4 5 6<br>
7 8 9<br>
<b>Matriz B:</b><br>
9 8 7<br>
6 5 4<br>
3 2 1<br>
<b>Saída:</b><br>
1848 2202 2556<br>
750 897 1044<br>
90 108 126<br>
</td>
<td>
<b>Caso 1:</b><br>
n = 3<br>
<b>Matriz A:</b><br>
1 2 3<br>
4 5 6<br>
7 8 9<br>
<b>Matriz B:</b><br>
9 8 7<br>
6 5 4<br>
3 2 1<br>
<b>Saída:</b><br>
1848 2202 2556<br>
750 897 1044<br>
90 108 126<br>
</td>
</tr>

</table>


<!-- ### Questão 1
Faça um programa em Python em que o usuário deverá informar três valores inteiros positivos, x, y e z. Os valores x e y, sendo x < y, formam um intervalo de valores inteiros. O valor de z deverá ser menor ou igual a y (z <= y). O programa deverá imprimir todos os valores inteiros compreendidos no intervalo [x, y] divisíveis por z. Após impressão, o programa deverá informar também a soma dos valores que são pares impressos.

<b>Exemplos:</b>

<b>Entradas 1:</b> x = 5, y = 19 e z = 3;<br>
<b>Saída 1:</b> 6 9 12 15 18, soma pares = 36

### Questão 2
Faça um programa em Python que leia um gabarito de uma prova com 10 questões, onde cada possui como resposta uma das alternativas: A, B, C, D ou E. Após ler o gabarito, o programa irá pedir o nome de um aluno e suas respostas dessa prova (cartão-resposta). Cada questão correta, o aluno soma pontos, de acordo com a tabela de pontuação a seguir:

<table>
<th>N° da questão</th>
<th>Pontuação</th>
<tr>
<td>1</td>
<td>15</td>
</tr>
<tr>
<td>2</td>
<td>15</td>
</tr>
<tr>
<td>3</td>
<td>15</td>
</tr>
<tr>
<td>4</td>
<td>15</td>
</tr>
<tr>
<td>5</td>
<td>20</td>
</tr>
<tr>
<td>6</td>
<td>20</td>
</tr>
<tr>
<td>7</td>
<td>20</td>
</tr>
<tr>
<td>8</td>
<td>30</td>
</tr>
<tr>
<td>9</td>
<td>30</td>
</tr>
<tr>
<td>10</td>
<td>30</td>
</tr>
</table>

Para cada questão errada, o aluno não soma pontos. O programa deverá informar o nome do aluno e a quantidade de pontos obtida na prova.

### Questão 3
Faça um programa que leia <b>n</b> valores inteiros positivos do usuário. O programa deverá informar se a sequência de valores digitada está em ordem crescente ou não.

<b>Exemplos:</b>

<b>Entradas 1:</b> n = 5, 6 9 12 17 18<br>
<b>Saída 1:</b> Está em ordem crescente!

<b>Entradas 2:</b> n = 11, 1 3 5 8 9 13 11 12 20 34 99<br>
<b>Saída 2:</b> Não está em ordem crescente! -->