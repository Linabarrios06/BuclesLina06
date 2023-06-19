#Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

num = int(input("Digitee la cantidad de estudiantes: "))

for i in range(num):
    print("Estudiante", i+1)
    nota1 = float(input("Digite la nota 1: "))
    nota2 = float(input("Digite la nota 2: "))
    nota3 = float(input("Digite la nota 3: "))

    notaMaxima = max(nota1, nota2, nota3)
    notaMinima = min(nota1, nota2, nota3)
    promedio = (nota1 + nota2 + nota3) / 3

    print(f"La nota más alta: {notaMaxima}")
    print(f"La nota más baja: {notaMinima}")
    print(f"El promedio: {promedio}")