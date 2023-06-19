#Sumar pares desde 0 hasta el numero que indique el usuario 

num = int(input("Digite un número: "))

suma = 0
for i in range(0, num + 1, 2):
    suma += i
print(f"La suma de los números pares de 0 hasta {num} es: {suma}")