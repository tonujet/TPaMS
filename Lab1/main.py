import numpy as np
from TaskB import *
from TaskC import *
from TaskA import *
import statistics as st

n = 121
mean_square_deviation = 1.3
sample = np.random.normal(0.0, mean_square_deviation, n).round(decimals=0)
# Variant
print("Variant: ", 120 % 11 + 11 * 5)



# Task A
print("------------Task А------------")
print("Це діаграма")
frequencies_polygon(sample, n)

# Task B
print("------------Task B------------")
print("Вибіркове середнє: ", round(sample_mean(sample), 3))
print(st.mean(sample))
print("Медіана: ", median(sample))
print(st.median(sample))
print("Мода: ", mode(sample))
print(st.multimode(sample))
print("Вибіркова дисперсія: ", round(sample_variance(sample), 3))
print(st.variance(sample))
print("Вибіркове середньоквадратичне відхилення: ", round(sample_mean_squared_deviation(sample), 3))
print(math.sqrt(st.variance(sample)))

# Task C
print("------------Task C------------")
print("Це діаграма")
build_graphics(10, sample)
