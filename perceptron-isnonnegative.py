from perceptron import perceptron

def is_nonnegative(x):
    return perceptron([x], [1], 0)

input = [5, 10, 2.5, 0.01, 0, -3, -7.8]

for i in input:
    classification = is_nonnegative(i)
    print(f"Input: {i:>10}, Classification: {classification}")