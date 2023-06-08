import math
import numpy as np
import scipy.stats as st
import Lab1.TaskB as stats


def mean_interval(sample, confidence, standard_deviation):
    n = len(sample - 1)
    alpha = 1 - confidence
    z = abs(st.norm.ppf(alpha / 2))
    mean = stats.sample_mean(sample)

    # interval bounds
    lower_bound = mean - z * standard_deviation / math.sqrt(n)
    upper_bound = mean + z * standard_deviation / math.sqrt(n)
    return lower_bound, upper_bound


def square_deviation_interval(sample, confidence):
    df = len(sample) - 1
    alpha = 1 - confidence
    standard_deviation = stats.sample_mean_squared_deviation(sample)

    # Нижній персинтиль
    chi2_lower = st.chi2.ppf(alpha / 2, df)

    # Верхній персинтиль
    chi2_upper = st.chi2.ppf(1 - alpha / 2, df)

    # Границі інтервалу
    lower_bound = np.sqrt(df * standard_deviation ** 2 / chi2_upper)
    upper_bound = np.sqrt(df * standard_deviation ** 2 / chi2_lower)

    return lower_bound, upper_bound
