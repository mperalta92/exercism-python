def get_factors(number):
    factors = []
    for i in range(1,number):
        if number % i == 0:
            factors.append(i)
    return factors

def aliquot_sum(number):
    aliquot_sum = 0
    for factor in get_factors(number):
        aliquot_sum += factor
    return aliquot_sum

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = aliquot_sum(number)
    if number == aliquot:
        return 'Perfect'
    if number < aliquot:
        return 'Abundant'
    return 'Deficient'
