#Hacer un programa que imprima la suna de todos los numeros impares desde 1 hasta n, y diga cuantos numeros impares hay 

num = int(input("Digite un numero: "))

suma = 1
contadorDeNumImpares = 1

for i in range(1, num+1, 2):
    suma += i
    contadorDeNumImpares += 1

print(f"La suma de los numeros impares de 1 hasta {num} es: {suma}")
print(f"La cantidad de numeros impares de 1 hasta {num} es: {contadorDeNumImpares}")