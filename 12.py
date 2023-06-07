pares = 0
impares = 0
sumaPares = 0
for i in range(1,5):
    print("Numero", i ,"de 4:")
    numero = int(input("Digite el numero--> "))
    if numero % 2 == 0:
        pares += 1
        sumaPares += numero
    else:
        impares += 1

print("numeros pares:", pares, "\nnumeros impares:", impares, "\nsuma de numeros:", sumaPares)
