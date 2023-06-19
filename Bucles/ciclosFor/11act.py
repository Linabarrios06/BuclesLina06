#Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.

cantidadDeTemperaturas = int(input("Digite el valor de las temperaturas : "))

if cantidadDeTemperaturas <= 0:
    print("Debe ingresar como minimo una temperatura ")
else:
    temperaturas = []
    for i in range(cantidadDeTemperaturas):
        temperatura = float(input("Digite la temperatura {}: ".format(i+1)))
        temperaturas.append(temperatura)

    temperaturaMaxima = max(temperaturas)
    temperaturaMinima = min(temperaturas)
    temperaturaPromedio = sum(temperaturas) / cantidadDeTemperaturas

    print(f"La temperatura más alta: {temperaturaMaxima}")
    print(f"La temperatura más baja: {temperaturaminima}")
    print(f"La temperatura promedio: {temperaturaPromedio}")