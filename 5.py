conversor = (input("Digite P para convertir dolares a pesos o D para convertir a dolares--> "))
conversor = conversor.lower()

if conversor == "d":
    monedaPesos = int(input("Digite el monto en pesos--> "))
    monedaDolares = monedaPesos / 485
    print(monedaPesos, "pesos son", monedaDolares, "dolares")

elif conversor == "p":
    monedaDolares = int(input("Digite el monto en dolares--> "))
    monedaPesos = monedaDolares * 485
    print(monedaDolares, "dolares son", monedaPesos, "pesos")


















