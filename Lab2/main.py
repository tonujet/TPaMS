from Task1 import *
from Task2 import *
import Lab1.TaskB as stats

n = 121
standard_deviation = 1.3
sample = np.random.normal(0.0, standard_deviation, n).round(decimals=2)
confidence = 0.95
# Variant
print("Variant: ", 120 % 11 + 11 * 5)



# Task A
print("\n\n\t\t\t\t------------Task 1------------\n")
print("Вибірка: ", sample)
print("\nВибіркове середнє: ", stats.sample_mean(sample))
print("Вибіркове середньоквадратичне відхилення: ",standard_deviation)

print("\nДвохсторонній довірчий інтервал для математичного сподівання з рівнем довіри 95%:\n",
      mean_interval(sample, confidence, standard_deviation))

print("\nДвохсторонній довірчий інтервал для середньоквадратичного відхилення з рівнем довіри 95%:\n",
      square_deviation_interval(sample, confidence))

# Task B
print("\n\n\t\t\t\t------------Task 2------------\n")


