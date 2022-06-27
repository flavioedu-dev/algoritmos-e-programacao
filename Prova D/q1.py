x = int(input("Digite o dia: "))
y = int(input("Digite o mês: "))
z = int(input("Digite o ano: "))

caso1 = [4, 6, 9, 11]
caso2 = [2]

val = 'INVÁLIDA!'

if (0< x <=31) and (0< y <=12) and (0< z <=2022):

    if y in caso1:
        if x<=30:
            val = 'VÁLIDA!'
        else:
            val = 'INVÁLIDA!'

    elif y in caso2:

        for i in range(0, z+1, 100):
            if z == i and z%4==0 and z%400==0:

                if x<=29:
                    val = 'VÁLIDA!'
                else:
                    val = 'INVÁLIDA!'

            elif z!=i and z%4==0:

                if x<=29:
                    val = 'VÁLIDA!'
                    
                else:
                    val = 'INVÁLIDA!'

            else:
                if x<28:
                    val = "VÁLIDA!"
                else:
                    val = "INVÁLIDA!"

    else:
        val = 'VÁLIDA!'

print("A data %i/%i/%i é %s" % (x, y, z, val))