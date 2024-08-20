from perceptron import train_perceptron, perceptron

xor_data = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 0),
]

xor_weights, xor_threshold = train_perceptron(xor_data)

print("AND Weights:", xor_weights)
print("AND Threshold:", xor_threshold)

print(perceptron((0,0), xor_weights, xor_threshold)) # prints 0
print(perceptron((0,1), xor_weights, xor_threshold)) # prints 0
print(perceptron((1,0), xor_weights, xor_threshold)) # prints 0
print(perceptron((1,1), xor_weights, xor_threshold)) # prints 1