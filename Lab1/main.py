import numpy as np
from TaskB import *

n = 121
mean_square_deviation = 1.3
sample = np.random.normal(0.0, mean_square_deviation, n)
print("Variant: ", 120 % 11 + 11 * 5)


# Task B
print("Вибіркове середнє: ", sample_mean(sample))
print("Медіана: ", median(sample))
print("Мода: ", mode(sample))
print("Вибіркова дисперсія: ", sample_variance(sample))
print("Вибіркове середньоквадратичне відхилення: ", sample_mean_squared_deviation(sample))










