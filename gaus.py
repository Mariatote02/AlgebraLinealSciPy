import numpy as np
from scipy import linalg
from fractions import Fraction

# Función para ingresar una matriz
def ingresar_matriz(filas, columnas, nombre="Matriz"):
    print(f"\nIngrese los valores de la {nombre} {filas}x{columnas}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

# Función para convertir a fracciones
def a_fracciones(matriz):
    return np.array([[Fraction(str(x)).limit_denominator() for x in fila] for fila in matriz])

print("=== Resolución de matrices con SciPy (Gauss y Pseudo-inversa) ===")

filas = int(input("Número de filas de la matriz A: "))
columnas = int(input("Número de columnas de la matriz A: "))
A = ingresar_matriz(filas, columnas, "Matriz A")

# Si es cuadrada: resolver inversa con Gauss
if filas == columnas:
    I = np.eye(filas)
    try:
        A_inv = linalg.solve(A, I)   # Inversa por Gauss
        print("\nMatriz inversa A^-1 en fracciones:")
        print(a_fracciones(A_inv))
    except Exception as e:
        print("\nError: la matriz no es invertible.")
        print(e)
# Si no es cuadrada: calcular pseudo-inversa
else:
    A_pinv = linalg.pinv(A)
    print("\nPseudo-inversa de A (porque no es cuadrada), en fracciones:")
    print(a_fracciones(A_pinv))
