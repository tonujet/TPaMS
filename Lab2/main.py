from Task1 import *
from Task2 import *

n = 121
mean_square_deviation = 1.3
sample = np.random.normal(0.0, mean_square_deviation, n).round(decimals=2)
# Variant
print("Variant: ", 120 % 11 + 11 * 5)



# Task A
print("------------Task 1------------")
print("Вибіркове середнє: ", st.mean(sample))
print("Вибіркове середньоквадратичне відхилення: ", round(st.stdev(sample), 3))

mean_interval = getMeanInterval(sample)
print("Проміжок для математичного сподівання з рівнем довіри 95%", mean_interval)

mean_square_deviation_interval = getSquareDeviationInterval(sample)
print("Проміжок для середньоквадратичного відхилення з рівнем довіри 95%", mean_square_deviation_interval)

# Task B
print("------------Task 2------------")


