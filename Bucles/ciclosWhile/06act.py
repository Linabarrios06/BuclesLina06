#Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

num = int(input("Digite la cantidad de notas: "))

sumaNotas = 0

for i in range(num):
    nota = float(input("Digite la nota {}: ".format(i+1)))
    sumaNotas += nota

promedio = sumaNotas / n

print(f"El promedio de las notas ingresadas son: {promedio}")