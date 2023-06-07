import math



# Вибіркове середнє
def sample_mean(sample):
    arr_sum = 0
    for number in sample:
        arr_sum += number
    return arr_sum / len(sample)


# Медіана
def median(sample):
    sample.sort()
    arr_len = len(sample)
    center_index = int(arr_len / 2)
    if arr_len % 2 == 0:
        right_central_index = center_index
        left_central_index = center_index - 1
        return (sample[right_central_index] + sample[left_central_index]) / 2
    return sample[center_index]


# Мода
def mode(sample):
    numbers_quantity = {}
    for number in sample:
        if number not in numbers_quantity:
            numbers_quantity[number] = 1
        else:
            numbers_quantity[number] = numbers_quantity[number] + 1
    return most_often_number(numbers_quantity)


def most_often_number(numbers_quantity):
    entries = numbers_quantity.items()
    maximum = max_value_in_dict(entries)
    return keys_with_max_value(entries, maximum)


def max_value_in_dict(entries):
    maximum = None
    for key, value in entries:
        if maximum is not None:
            if value > maximum:
                maximum = value
        else:
            maximum = value
    return maximum


def keys_with_max_value(entries, maximum):
    res = []
    for key, value in entries:
        if value == maximum:
            res.append(key)

    if len(res) == 1:
        return res[0]
    return res


# Вибіркова дисперпсія
def sample_variance(sample):
    square_number_sum = 0
    s_mean = sample_mean(sample)
    for number in sample:
        square_number_sum += number ** 2
    numerator = square_number_sum - len(sample) * (s_mean ** 2)
    denominator = len(sample) - 1
    return numerator / denominator


# Вибіркове середньоквадратичне відхилення
def sample_mean_squared_deviation(sample):
    return math.sqrt(sample_variance(sample))
