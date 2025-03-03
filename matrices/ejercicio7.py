# Llenar array bidimensional con notas de estudiantes
clases = 3
alumnos = 5  # Puedes cambiar este número (máximo 30)
notas = []

for i in range(clases):
    print(f"Introduce las notas de los alumnos para la clase {i+1}:")
    clase = [float(input(f"Nota del alumno {j+1}: ")) for j in range(alumnos)]
    notas.append(clase)

# Visualizar el array
print("\nNotas de las clases:")
for i, clase in enumerate(notas):
    print(f"Clase {i+1}: {clase}")

# Calcular nota máxima y mínima
nota_max = max(max(clase) for clase in notas)
nota_min = min(min(clase) for clase in notas)

# Encontrar estudiantes y clases con la nota máxima y mínima
print("\nNota máxima y mínima:")
for i, clase in enumerate(notas):
    for j, nota in enumerate(clase):
        if nota == nota_max:
            print(f"Máxima: {nota_max} en Clase {i+1}, Alumno {j+1}")
        if nota == nota_min:
            print(f"Mínima: {nota_min} en Clase {i+1}, Alumno {j+1}")
