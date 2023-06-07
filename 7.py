ladoUno = int(input("Digite la primera medida de tu triangulo--> "))
ladoDos = int(input("Digite la segunda medida de tu triangulo--> "))
ladoTres = int(input("Digite la tercera medida de tu triangulo--> "))

if ladoUno == ladoDos == ladoTres:
    print("el triangulo es equilátero")
elif ladoUno != ladoDos != ladoTres:
    print("el triangulo es escaleno")
else:
    print("el triangulo es isosceles")