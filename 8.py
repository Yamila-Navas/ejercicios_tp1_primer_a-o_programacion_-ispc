monto = int(input("Digite el monto de su compra--> "))
opcionDePago = int(input("Digite 1 para pagar de contado, 2 para pagar con targeta, 3 para pagar con debito--> "))
if opcionDePago == 1:
    descuento = monto * 10 / 100
    montoTotal = monto - descuento
    print("monto:", monto, "\ndescuento:",descuento, "\nmonto total:", montoTotal)
elif opcionDePago == 2:
    interes = monto * 10 / 100
    montoTotal = monto + interes
    print("monto:", monto, "\ninteres:",interes, "\nmonto total:", montoTotal)
elif opcionDePago == 3:
    descuento = monto * 5 / 100
    montoTotal = monto - descuento
    print("monto:", monto, "\ndescuento:",descuento, "\nmonto total:", montoTotal)