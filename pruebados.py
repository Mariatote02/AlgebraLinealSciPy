import numpy as np
from scipy import linalg

# Función para ingresar una matriz
def ingresar_matriz(filas, columnas, nombre="matriz"):
    print(f"\nIngrese los valores de la {nombre} {filas}x{columnas}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

# Menú de operaciones
print("Seleccione la operación:")
print("1. Suma de matrices")
print("2. Resta de matrices")
print("3. Multiplicación de matrices")
print("4. Producto escalar de matrices")
op = int(input("Opción: "))

# Suma y Resta de matrices
if op in [1, 2]:
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    A = ingresar_matriz(filas, columnas, "Matriz A")
    B = ingresar_matriz(filas, columnas, "Matriz B")

    if op == 1:
        print("\nResultado de la suma:")
        print(A + B)
    else:
        print("\nResultado de la resta:")
        print(A - B)

# Multiplicación de matrices
elif op == 3:
    filas_A = int(input("Número de filas de la Matriz A: "))
    columnas_A = int(input("Número de columnas de la Matriz A: "))
    filas_B = int(input("Número de filas de la Matriz B: "))
    columnas_B = int(input("Número de columnas de la Matriz B: "))

    if columnas_A != filas_B:
        print("\nNo se puede multiplicar: columnas de A ≠ filas de B")
    else:
        A = ingresar_matriz(filas_A, columnas_A, "Matriz A")
        B = ingresar_matriz(filas_B, columnas_B, "Matriz B")
        print("\nResultado de la multiplicación:")
        print(np.dot(A, B))

# Producto escalar de matrices (Hadamard)
elif op == 4:
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))

    # Validar condición filas >= columnas
    if filas < columnas:
        print("\nNo se puede realizar el producto escalar: filas < columnas")
    else:
        # Ingresar matrices
        A = ingresar_matriz(filas, columnas, "Matriz A")
        B = ingresar_matriz(filas, columnas, "Matriz B")

        # Pedir la operación
        print("\nEscriba la operación (ejemplo: 2*A - B , 3*A + 2*B):")
        expr = input("Operación: ")

        # Evaluar la operación de forma segura
        try:
            resultado = eval(expr, {"A": A, "B": B, "np": np})
            print("\nResultado de la operación:")
            print(resultado)
        except Exception as e:
            print("\nError en la operación:", e)

else:
    print("Opción no válida.")

