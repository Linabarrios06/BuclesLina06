#Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

suma = 0

while True:
    num = int(input("Digite un numero entero (Digite 0 para finalizar): "))

    if num == 0:
        break

    suma += num

print(f"El total de la suma de los numeros ingresados es: {suma}")