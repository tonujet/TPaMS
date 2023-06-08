import math
import numpy as np
import scipy.stats as st
import Lab1.TaskB as stats


def mean_interval(sample, confidence):
    n = len(sample - 1)
    alpha = 1 - confidence
    z = abs(st.t.ppf(alpha / 2, n - 1))
    mean = stats.sample_mean(sample)
    standard_deviation = stats.sample_mean_squared_deviation(sample)
    lower_bound = mean - z * standard_deviation / math.sqrt(n)
    upper_bound = mean + z * standard_deviation / math.sqrt(n)
    return lower_bound, upper_bound


def library_mean_interval(sample, confidence):
    mean_interval = st.norm.interval(confidence=confidence, loc=stats.sample_mean(sample), scale=st.sem(sample))
    return mean_interval


def square_deviation_interval(sample, confidence):
    df = len(sample) - 1
    alpha = 1 - confidence
    standard_deviation = stats.sample_mean_squared_deviation(sample)

    chi2_lower = st.chi2.ppf(alpha / 2, df)
    chi2_upper = st.chi2.ppf(1 - alpha / 2, df)

    lower_bound = np.sqrt(df * standard_deviation ** 2 / chi2_upper)
    upper_bound = np.sqrt(df * standard_deviation ** 2 / chi2_lower)

    return lower_bound, upper_bound

# def library_square_deviation_interval(sample, confidence):
    # return st.t.interval(confidence, len(sample)-1, loc=np.mean(sample), scale=st.sem(sample))
