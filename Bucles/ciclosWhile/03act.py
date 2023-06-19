#Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

num = int(input("Digite un numero: "))

sumaImpares = 0
cantidadNumImpares = 0
enumerador = 1

while enumerador <= num:
    if enumerador % 2 != 0:
        sumaImpares += enumerador
        cantidadNumImpares += 1
    enumerador += 1

print(f"La suma de numeros impares de 1 hasta {num} es: {sumaImpares}")
print(f"La cantidad de numeros impares es: {cantidadNumImpares}")