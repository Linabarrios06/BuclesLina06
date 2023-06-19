#Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero

num = int(input("Digite un numero entero, mayor ha cero: "))

if num <= 0:
    print("El numero debe ser mayor ha cero")
else:
    print(f"Los divisores de {num} son:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)