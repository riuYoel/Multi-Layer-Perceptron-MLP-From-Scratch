yoel_features = [4, 5, 5]
integration_biases = [-55, -35, -45]

def dot_product(vector_a,vector_b):
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total

def matrix_vector_multiply(matrix,vector):
    matrix_output = []
    for rows in matrix:
        total_matrix = dot_product(rows, vector)
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

enterprises = [
    [5,4,2],
    [2,3,4],
    [4,5,5]
]

result_a = matrix_vector_multiply(enterprises,yoel_features)
result_b = add_bias(result_a, integration_biases)
relu_filter = relu(result_b)
print(f"First raw result: {result_a}, after bias: {result_b}, after relu: {relu_filter}")