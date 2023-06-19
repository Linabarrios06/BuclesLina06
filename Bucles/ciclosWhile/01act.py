#Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos

num = int(input("Digite un numero: "))

total = 0

if num > 10:
    enumerador = 1
    while enumerador <= 10:
        resultado *= enumerador
        enumerador += 1
else:
    enumerador = 1
    while enumerador <= num:
        total += enumerador
        enumerador += 1
print(f"El resultado es: {total}")