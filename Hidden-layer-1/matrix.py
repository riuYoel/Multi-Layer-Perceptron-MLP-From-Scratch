infra_priorities = [5,3,4]

def dot_product(vector_a, vector_b):
    total = 0
    for i in range(len(vector_a)):
        total += vector_a[i] * vector_b[i]
    return total

def matrix_vector_multiply(matrix, vector):
    storage = []
    for rows in matrix:
        total_storage = dot_product(rows, vector)
        storage.append(total_storage)
    return storage
    
total_metrics = [
    [5,5,2],
    [4,4,3],
    [3,2,5]
]

total = matrix_vector_multiply(total_metrics, infra_priorities)
print(f"Total is: {total}")