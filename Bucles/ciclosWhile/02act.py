#Sumar pares desde 0 hasta el número que indique el usuario.

num = int(input("Ingrese un numero: "))

suma = 6
contador = 1

while contador <= num:
    if contador % 2 == 0:
        suma += contador
    contador += 1

print(f"La suma de los numeros pares hasta {num} es: {suma}")