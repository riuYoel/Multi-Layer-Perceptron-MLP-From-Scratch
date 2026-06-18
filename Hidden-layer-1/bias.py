yoel_priorities = [5,3,4]
project_biases = [-30, -35, -40]

def dot_product(vector_a, vector_b):
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total

def matrix_vector_multiply(matrix, vector):
    matrix_output = []
    for rows in matrix:
        matrix_result = dot_product(rows, vector)
        matrix_output.append(matrix_result)
    return matrix_output

def add_bias(vector, bias_vector):
    bias_output = []
    for i in range(len(vector)):
        bias_result = vector[i] + bias_vector[i]
        bias_output.append(bias_result)
    return bias_output

startups_inversion = [
[3,2,5],
[4,5,1],
[5,1,4]
]

result_a = matrix_vector_multiply(startups_inversion,yoel_priorities)
result_b = add_bias(result_a, project_biases)
print(f"Result: {result_a}, result after bias: {result_b}")

