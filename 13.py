mayores = 0
menores = 0
minimo = 1000
maximo = 0

for i in range(1,11):
    print("Numero", i ,"de 10:")
    numero = int(input("Digite el numero--> "))
    if numero > 100:
        mayores += 1
        if numero > maximo:
            maximo = numero
    else:
        menores +=1
        if numero < minimo:
            minimo = numero

print("cantidad de mayores a 100:", mayores, "\ncantidad de menores a 100:", menores, "\nminimo alcanzado:", minimo,"\nmaximo alcanzado:", maximo)
  
