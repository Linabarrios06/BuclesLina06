#Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

num = int(input("Digite la cantidad de estudiantes: "))

if num <= 0:
    print("Digite como minimo un estudiante ")
else:
    notasMasAltas = []
    notasMasBajas = []
    promedios = []

    for i in range(num):
        print(f"Digite las notas del estudiante {i+1}")
        notas = []
        for j in range(4):
            nota = float(input("Digite la nota {}: ".format(j+1)))
            notas.append(nota)

        promedio = sum(notas) / len(notas)
        promedios.append(promedio)

        notaMaxima = max(notas)
        notasMasAltas.append(notaMaxima)

        notaMinima = min(notas)
        notasMasBajas.append(notaMinima)

    notaMaximaTotal = max(notasMasAltas)
    notaMinimaTotal = min(notasMasBajas)
    promedioTotal = sum(promedios) / len(promedios)

    print(f"Nota más alta: {notaMaximaTotal}")
    print(f"Nota más baja: {notaMinimaTotal}")
    print(f"Promedio general: {promedioTotal}")