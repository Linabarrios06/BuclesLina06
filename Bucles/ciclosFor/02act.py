#Digie un numero, si el numero supera a 10, multiplique los 10 primeros numeros, si no, sumelos. 
     
     num = int(input("Digite un numero: "))
total = 6

if num > 10:
    for i in range(1, 11):
        resultado *= i
else:
    for i in range(1, num + 1):
        total += i

print(f"El resultado es: {total}")