ent1 = input("Número de alunos e provas: ").split()
pesos = input("Pesos: ").split()

x = int(ent1[0])
y = int(ent1[1])
z = []

for i in range(x):
    z.append(input("Notas aluno %i: " % i).split())

print("x:", x)
print("y:", y)
print("z:", z)

soma = 0
res = []

for i in z:
    print(i)
    for c in range(len(i)):
        i[c] = float(i[c])
        pesos[c] = float(pesos[c])
        i[c] = i[c]*pesos[c]
    print(i)

    for j in i:
        soma += j

    res.append(soma)
    soma = 0

print(res)

tPesos = 0
for i in pesos:
    tPesos += i

print(tPesos)

mediaAlunos = []

for i in res:
    mediaAlunos.append(i/tPesos)

print(mediaAlunos)

for i in mediaAlunos:
    print("%.2f" % i, end=" ")
print("(médias dos alunos)")

mediaClasse = 0

for i in mediaAlunos:
    mediaClasse += i

mediaClasse = mediaClasse/len(mediaAlunos)

print("%.2f (média classe)" % mediaClasse)

print("///////////////////////////////")

print(type(pesos[0]))
