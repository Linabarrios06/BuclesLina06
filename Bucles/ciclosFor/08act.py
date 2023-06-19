#Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

num = int(input("Digite la cantidad de notas del estudiante: "))

notas = []
for i in range(num):
    nota = float(input("Digite la nota {}: ".format(i+1)))
    notas.append(nota)

promedio = sum(notas) / num

print(f"El promedio del estudiante es: {promedio}")