#Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero

num = int(input("Digite un numero entero mayor que cero: "))

while num <= 0:
    num = int(input("Numero inválido. Ingrese un numero entero mayor que cero: "))

print(f"Divisores de {num} :")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)