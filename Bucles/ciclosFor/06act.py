#Hacer un programa que pida dos numeros y muestre todos los numeros que van desde el primero al segundo, validar u el primer numero sea menor que el segundo

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num1 >= num2:
    print(f"El primer numero debe ser menor que el segundo numero.")
else:
    for i in range(num1, num2 + 1):
        print(i)