import math

import numpy as np
import scipy.stats as st

from Task1 import *


# Повертає залежність оцінки від рівня довіри для мат сподівання
def intervals_for_diff_confidence_for_mi(sample, standard_deviation, conf_diff=0.1, start_conf_value=0):
    result = {}
    confidence = start_conf_value + conf_diff

    while round(confidence, 3) < 1:
        result[round(confidence, 3)] = mean_interval(sample, confidence, standard_deviation)
        confidence += conf_diff

    return result


# Повертає залежність оцінки від рівня довіри для середньоквадратичного відхилення
def intervals_for_diff_confidence_for_sdi(sample, conf_diff=0.1, start_conf_value=0):
    result = {}
    confidence = start_conf_value + conf_diff

    while round(confidence, 3) < 1:
        result[round(confidence, 3)] = square_deviation_interval(sample, confidence)
        confidence += conf_diff

    return result


# Повертає залежність оцінки від обсягу вибірки для мат сподівання
def intervals_for_diff_sample_size_for_mi(standard_deviation, max_size=80, diff_size=10):
    result = {}
    n = diff_size

    while n <= max_size:
        sample = np.random.normal(0.0, standard_deviation, n).round(decimals=2)
        result[n] = mean_interval(sample, 0.95, standard_deviation)
        n += diff_size

    return result


# Повертає залежність оцінки від рівня довіри для середньоквадратичного відхилення
def intervals_for_diff_sample_size_for_sdi(standard_deviation, max_size=80, diff_size=10):
    result = {}
    n = diff_size

    while n <= max_size:
        sample = np.random.normal(0.0, standard_deviation, n).round(decimals=2)
        result[n] = square_deviation_interval(sample, 0.95)
        n += diff_size

    return result


def dict_printer(dict):
    for key, value in dict.items():
        print(key, ' : ', value)
