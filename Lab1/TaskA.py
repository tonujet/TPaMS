import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt


def frequencies_polygon(sample, n):
    sample.sort()
    l = 1

    for i in range(len(sample)):
        number = round(sample[i], 1)
        if i + 1 < n:
            if number < round(sample[i + 1], 1):
                l += 1
            else:
                continue

    polygon_sample = [0] * l
    m = 0

    for i in range(len(sample)):
        number = round(sample[i], 1)
        if i + 1 < n:
            if round(sample[i + 1], 1) == number:
                continue
        polygon_sample[m] = number
        m += 1

    frequencies = [0] * l
    k = 0

    for i in range(len(sample)):
        number = round(sample[i], 1)
        if i + 1 < n:
            if round(sample[i + 1], 1) == number:
                continue
        temp = 0
        for j in range(len(sample)):
            if number == round(sample[j], 1):
                temp += 1
        frequencies[k] = temp
        k += 1
    plt.xlabel('value')
    plt.ylabel('frequency')
    x = plt.hist(sample, bins=l)
    x_array = valueForFrequenciPoligon(x[1])
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.plot(x_array, frequencies)
    plt.show()


def valueForFrequenciPoligon(x_array):
    result = []

    for j in range(len(x_array) - 1):
        result.append((x_array[j] + x_array[j + 1]) / 2)

    return result
