from perceptron import train_perceptron, perceptron

and_data = [
    ((0, 0), 0),
    ((0, 1), 0),
    ((1, 0), 0),
    ((1, 1), 1),
]

and_weights, and_threshold = train_perceptron(and_data)

print("AND Weights:", and_weights)
print("AND Threshold:", and_threshold)

print(perceptron((0,0),and_weights,and_threshold)) # prints 0
print(perceptron((0,1),and_weights,and_threshold)) # prints 0
print(perceptron((1,0),and_weights,and_threshold)) # prints 0
print(perceptron((1,1),and_weights,and_threshold)) # prints 1