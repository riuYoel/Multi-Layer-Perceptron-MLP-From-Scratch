def dot_product(vector_a, vector_b):
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total

def matrix_vector_multiply(matrix, vector):
    matrix_output = []
    for row in matrix:
        total_matrix = dot_product(row, vector)
        matrix_output.append(total_matrix)
    return matrix_output

def add_bias(vector, bias_vector):
    bias_output = []
    for i in range(len(vector)):
        total_bias = vector[i] + bias_vector[i]
        bias_output.append(total_bias)
    return bias_output

def relu(vector):
    relu_output = []
    for number in vector:
        if number > 0:
            relu_output.append(number)
        else:
            relu_output.append(0)
    return relu_output


# Input vector
datos_actuales = [4, 5, 5] 

red_neuronal = [
    # Capa 1 Matriz inventada e input
    ([[5,4,2], [2,3,4], [4,4,5]], [-55,-35,-45]),
    # [Capa 2: Matrices inventadas
    ([[6,1,8], [9,3,1], [9,1,3]], [-70,-60,-40]),
    # [Capa 3: Matrices inventadas
    ([[3,2,1], [3,3,3], [6,7,6]], [-40,-30,-50]),
    # [Capa 4: Matrices inventadas
    ([[5,8,3], [7,6,2], [5,3,7]], [-60,-60,-40]),
    # [Capa 5: Matrices inventadas
    ([[4,3,4], [1,6,2], [6,3,2]], [-30,-25,-40]),
    # [Capa 6: Matrices inventadas
    ([[8,2,2], [1,8,8], [6,7,6]], [-50,-30,-50]),
    # [Capa 7: Matrices inventadas
    ([[9,6,6], [4,6,3], [6,6,7]], [-80,-60,-70]),
    # [Capa 8: Matrices inventadas
    ([[1,7,4], [1,6,2], [6,7,2]], [-30,-25,-60]),
    # [Capa 9: Output
    ([[2,9,9]], [-60])
]    


for i, (pesos, biases) in enumerate(red_neuronal,start=1):
    paso_a = matrix_vector_multiply(pesos, datos_actuales)
    paso_b = add_bias(paso_a, biases)
    datos_actuales = relu(paso_b)
    print(f"Capa {i} procesada con exito. Datos actuales: {datos_actuales}")

