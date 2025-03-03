# Datos: 3 asignaturas x 15 alumnos
notas = []
print("Introduce las notas de cada asignatura para 15 alumnos:")
for i in range(3):
    fila = list(map(float, input(f"Asignatura {i+1} (15 notas separadas por espacio): ").split()))
    notas.append(fila)

# Media por alumno
medias_alumnos = [sum(col) / len(col) for col in zip(*notas)]
print("\nNota media del alumno:")
for i, media in enumerate(medias_alumnos):
    print(f"Alumno {i+1}: {media:.2f}")

# Media por asignatura
medias_asignaturas = [sum(fila) / len(fila) for fila in notas]
print("\nNota media por asignatura:")
for i, media in enumerate(medias_asignaturas):
    print(f"Asignatura {i+1}: {media:.2f}")

# Media de toda la clase
media_clase = sum(medias_asignaturas) / len(medias_asignaturas)
print(f"\nNota media de la clase: {media_clase:.2f}")
