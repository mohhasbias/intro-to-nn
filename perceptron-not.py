from perceptron import perceptron


def not_function(x):
    weight = -1
    threshold = -0.5
    return perceptron([x], [weight], threshold)

print("NOT(0):", not_function(0))  # Outputs: 1
print("NOT(1):", not_function(1))  # Outputs: 0