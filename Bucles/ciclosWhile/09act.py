#Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio.

num = int(input("Digite la cantidad de temperaturas: "))

temperaturas = []
sumaTemperaturas = 0
enumerador = 0

while enumerador < num:
    temperatura = float(input("Digite la temperatura {}: ".format(enumerador + 1)))
    temperaturas.append(temperatura)
    sumaTemperaturas += temperatura
    enumerador += 1

temperaturaMaxima = max(temperaturas)
temperaturaMinima = min(temperaturas)
promedioTemperaturas = sumaTemperaturas / num

print(f"La emperatura más alta: {temperaturaMaxima}")
print(f"La temperatura más baja: {temperaturaMinima}")
print(f"La temperatura promedio: {promedioTemperaturas}")