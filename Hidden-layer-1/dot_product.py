saas_priorities = [5,5,3,4]
idea_metrics = [4,2,5,3]

def dot_product(saas_priorities, idea_metrics):
    total = 0
    for i in range(len(saas_priorities)):
        total += saas_priorities[i] * idea_metrics[i]
    return total

result = dot_product(saas_priorities, idea_metrics)
print("And the result is: ", result)