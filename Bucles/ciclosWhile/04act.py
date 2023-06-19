#Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num1 >= num2:
    print("***Error***  El primer numero debe ser menor que el segundo numero.")
else:
    enumerador = num1
    while enumerador <= num2:
        print(enumerador)
        enumerador += 1
