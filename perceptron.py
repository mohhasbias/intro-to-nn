import random


def perceptron(inputs, weights, threshold):
    weighted_sum = sum([i * w for i, w in zip(inputs, weights)])
    return 1 if weighted_sum >= threshold else 0

def train_perceptron(data, learning_rate=0.01, max_iter=1000):
    first_pair = data[0]
    num_inputs = len(first_pair[0])

    weights = [random.random() for _ in range(num_inputs)]
    threshold = random.random()

    for _ in range(max_iter):
        num_errors = 0
        for inputs, target in data:
            output = perceptron(inputs, weights, threshold)
            error = target - output
            if error != 0:
                num_errors += 1
                for i in range(num_inputs):
                    weights[i] += learning_rate * error * inputs[i]
                threshold -= learning_rate * error

        if num_errors == 0:
            break

    return weights, threshold