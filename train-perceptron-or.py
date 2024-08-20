from perceptron import train_perceptron, perceptron

or_data = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 1),
]

or_weights, or_threshold = train_perceptron(or_data)

print("AND Weights:", or_weights)
print("AND Threshold:", or_threshold)

print(perceptron((0,0), or_weights, or_threshold)) # prints 0
print(perceptron((0,1), or_weights, or_threshold)) # prints 0
print(perceptron((1,0), or_weights, or_threshold)) # prints 0
print(perceptron((1,1), or_weights, or_threshold)) # prints 1