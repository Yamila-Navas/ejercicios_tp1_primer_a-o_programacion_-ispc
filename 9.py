primerNumero = int(input("Digite el primer numero--> "))
segundoNumero = int(input("Digite el sugundo numero--> "))
tercerNumero = int(input("Digite el tercer numero--> "))

if primerNumero > segundoNumero:
    if primerNumero > tercerNumero:
        print(primerNumero, "es mayor")
    else:
        print(tercerNumero, "es mayor")
elif segundoNumero > primerNumero:
    if segundoNumero > tercerNumero:
        print(segundoNumero, "es mayor")
    else:
        print(tercerNumero, "es mayor")       