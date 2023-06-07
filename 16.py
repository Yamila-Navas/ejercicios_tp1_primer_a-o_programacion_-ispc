lista = []

for i in range(1,5):
    numero = int(input("Digite un numero negativo--> "))
    if numero < 0:
        positivo = abs(numero)
        lista.append(positivo)
        

print("convercion a positivos:",lista)


#agregue una lista para visualisar todos los numeros digitados.
