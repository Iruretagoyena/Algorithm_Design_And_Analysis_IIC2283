import time
import sys


def multiply(matrix, vector):
    result = []
    for matrix_idx in range(len(matrix[0])):
        vector_total_j = 0
        for vector_idx in range(len(vector)):
            vector_total_j += vector[vector_idx] * matrix[vector_idx][matrix_idx]
        result.append(vector_total_j)
    return result


def power(matrix, vector, to_the_n):
    res = multiply(matrix, vector)
    to_the_n -= 1
    while to_the_n >= 1:
        res = multiply(matrix, res)
        to_the_n -= 1
    return res


def calculate_power_matrix(n_edges):
    adjacency_matrix = [
        [0, 2, 2, 1],
        [2, 0, 0, 1],
        [2, 0, 0, 1],
        [1, 1, 1, 0]
    ]

    movement_vector = [1, 1, 1, 1]

    move_n_steps = power(adjacency_matrix, movement_vector, n_edges)
    total_steps = sum(move_n_steps)

    return total_steps


def kalingrado(n_edges):
    dp = [0]
    dp[0] = 4

    if n_edges == 0:
        return dp[n_edges]

    return calculate_power_matrix(n_edges) % (10 ** 9 + 7)


n_edges = list(map(int, sys.stdin.readline().strip().split()))
result = kalingrado(n_edges[0])
sys.stdout.write(str(result))


"""

Contar cantidad de caminos distintos de largo N en el multigrafo dado

Opciones
1. Brute force
2. optimizado log n tiempo usando factorización matricial
3. optimizado o(1) espacio usando DP

Inspiración
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

De acá aprendí que podemos usar multiplicacion matricial para hacer log n tiempo
O((V+E)log(n)) con V+E constante, entonces O(log(n)) 

De acá reconfirmé que se puede lograr con la potencia de la matriz
https://iq.opengenus.org/number-of-paths-with-k-edges/

Solo quedaba una cosa por optimizar...

power in log n
https://cs.stackexchange.com/questions/4998/is-there-a-olog-n-algorithm-for-matrix-exponentiation
https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/






Ideas

    largo = 1
    Vector 1,1,1,1
    x 
    matriz de transiciones
    el siguiente estado me lo da 
    
    dos estados mas adelante
    
    calcular la potencia de la matriz
    
        adjacency_matrix = [
        [0, 2, 2, 1],
        [2, 0, 0, 1],
        [2, 0, 0, 1],
        [1, 1, 1, 0]
    ]

        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
        
Tip
Piense en una solucion usando programacion dinamica con complejidad O(N) con una tabla de O(N) elementos.
Luego piense en como optimizarla para que la tabla sea de O(1) elementos, para despues reformular
la recurrencia de la solucion con una matriz.


"""


"""
MATHPOWER (M, n)
if n == 1
    then return M
else
    P = MATHPOWER (M, floor(n/2))
    if n mod 2 == 0
        then return P * P
    else
        return P * P * M

def power(x,y):
    temp = 0
    if( y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0)
        return temp * temp;
    else
        return x * temp * temp;


def power(matrix, vector, to_the_n):
    if to_the_n == 1:
        res_un = multiply_matrix_by_vector(matrix, vector)
        return res_un

    P = multiply_matrix_by_matrix(matrix, matrix)
    print("P", P)

    if to_the_n % 2 == 0:
        print("hi")
        return multiply_matrix_by_matrix(P, P)

    else:
        print("hey")
        mat_ = multiply_matrix_by_matrix(P, P)
        print("mat_", mat_)
        res = multiply_matrix_by_vector(mat_, vector)
        return res


def multiply_matrix_by_vector(matrix, vector):
    result_vector = []

    for matrix_idx in range(len(matrix[0])):
        vector_total_j = 0
        for vector_idx in range(len(vector)):
            vector_total_j += vector[vector_idx] * matrix[vector_idx][matrix_idx]
        result_vector.append(vector_total_j)

    return result_vector


def multiply_matrix_by_matrix(matrix_a, matrix_b):
    print(matrix_a)
    matrix_size = len(matrix_a[0])
    result_matrix = [[0] * matrix_size] * matrix_size
    mul = [[0] * matrix_size] * matrix_size

    for i in range(matrix_size):
        for j in range(matrix_size):
            mul[i][j] = 0
            for k in range(matrix_size):
                mul[i][j] += matrix_a[i][k] * matrix_b[k][j]

    for i in range(matrix_size):
        for j in range(matrix_size):
            result_matrix[i][j] = mul[i][j]

    return result_matrix


"""