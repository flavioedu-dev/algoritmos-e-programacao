""" lista = ["a", "b", "c", "d", "e"]

try:
    x = lista.index("A")
except:
    x = -1

print(x) """

""" numbers = [1, 3, 5, 8, 9, 13, 11, 12, 20, 34, 99]

numbers.sort() 

print(numbers) """

""" lista = []
i = 100

while i <2022:
    lista.append(i)
    i += 100

print(lista) """

z = 400

for i in range(100, z+1, 100):
    if z == i and z%4==0 and z%400==0:
        print('Bissexto')
