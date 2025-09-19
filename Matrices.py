import random
import time
from tabulate import tabulate

inicio = time.time()
alumnos = [[random.randint(50, 100) for _ in range(6)] for _ in range(500)]
fin = time.time()
print(f"\n⏱ Tiempo de generación de datos: {fin - inicio:.6f} segundos")

headers_forma1 = [f"Materia {i}" for i in range(1, 7)]
print("\n=== TABLA DE ALUMNOS (Alumnos en filas, Materias en columnas) ===")
print(tabulate(alumnos, headers=headers_forma1,
               showindex=[f"Alumno {i}" for i in range(1, 501)]))


alumno = 321
materia = 5
valor = alumnos[alumno - 1][materia - 1]
print("\n=== RESULTADO DE LA BÚSQUEDA ===")
print(f"El valor del Alumno {alumno} en la Materia {materia} es: {valor}")


inicio = time.time()
transpuesta = list(zip(*alumnos))
fin = time.time()
print(f"\n⏱ Tiempo de transposición: {fin - inicio:.6f} segundos")

headers = [f"Alumno {i+1}" for i in range(len(alumnos))]
tabla = [[f"Materia {j+1}"] + list(transpuesta[j]) for j in range(6)]

print("\n=== TABLA DE MATERIAS (Materias en filas, Alumnos en columnas) ===")
print(tabulate(tabla, headers=["Materia"] + headers, tablefmt="grid"))


print("\n📌 Resultado de la búsqueda:")
print(f"El alumno {alumno} tiene {alumnos[alumno-1][materia-1]} en la materia {materia}.")
