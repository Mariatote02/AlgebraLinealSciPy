import numpy
import scipy

import numpy as np
from scipy import linalg

# Menú para elegir tipo de matriz
print("Seleccione el tipo de matriz:")
print("1. 2x2")
print("2. 3x3")
print("3. 2x3")
opcion = int(input("Opción: "))

# Asignar dimensiones según elección
if opcion == 1:
    filas, columnas = 2, 2
elif opcion == 2:
    filas, columnas = 3, 3
elif opcion == 3:
    filas, columnas = 2, 3
else:
    print("Opción no válida")
    exit()

# Ingresar matriz
print(f"Ingrese los valores de la matriz {filas}x{columnas}:")
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Elemento ({i+1},{j+1}): "))
        fila.append(valor)
    matriz.append(fila)

A = np.array(matriz)
print("\nMatriz ingresada:")
print(A)

# Operaciones
print("\n--- Resultados ---")

# Determinante (solo si es cuadrada)
if filas == columnas:
    det = linalg.det(A)
    print(f"Determinante: {det}")

    if det != 0:
        inv = linalg.inv(A)
        print("\nInversa:")
        print(inv)
    else:
        print("\nLa matriz no es invertible.")

# Transpuesta
print("\nTranspuesta:")
print(A.T)

# Rango
rango = np.linalg.matrix_rank(A)
print(f"\nRango de la matriz: {rango}")

# Resolver sistema (solo si es cuadrada)
if filas == columnas:
    print("\n--- Resolviendo sistema Ax = b ---")
    b = []
    for i in range(filas):
        valor_b = float(input(f"Valor de b{i+1}: "))
        b.append(valor_b)
    b = np.array(b)
    if linalg.det(A) != 0:
        x = linalg.solve(A, b)
        print("Solución del sistema:")
        print(x)
    else:
        print("No se puede resolver el sistema, la matriz no es invertible.")
