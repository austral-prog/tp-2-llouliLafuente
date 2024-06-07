def change():
   gasto = float(input("Ingresar gasto: "))
    pago = float(input("Dinero recibido: "))
    pesos = pago - gasto
    centavos = float(pesos) - int(pesos)
    return pesos, int(centavos * 100)

cambio = change()
print("")
print("Vuelto")
print("")
print("Pesos: ", cambio[0])
print("Centavos: ", cambio[1])
