#Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.

tablaDeMultiplicacion = int(input("Digite el numero de la tabla de multiplicacion que desea ver: "))

print(f"Tabla de multiplicar del numero = {tablaDeMultiplicacion}")
for i in range(11):
    resultado = tablaDeMultiplicacion * i
    print(tablaDeMultiplicacion, "x", i, "=", resultado)