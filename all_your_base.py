
def divide(number, output_base):
    quotient = int(number/output_base)
    remainder = number%output_base
    return quotient, remainder

def decimal_to_output_base(decimal, output_base):
    result = []
    number = decimal
    while number > 0:
        quotient, remainder = divide(number, output_base)
        result.append(remainder)
        number = quotient
    result.reverse()
    return result

def map_input_base_to_decimal(digit):
    if str(digit).isalpha():
        return ord(digit) - ord('A') + 10
    return int(digit)

def input_base_to_decimal(input_base, digits):
    result = 0
    max_pow = len(digits) - 1
    for index, digit in enumerate(digits):
        value = map_input_base_to_decimal(digit)
        if value >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        result += value*(input_base**(max_pow - index))
    return result
    
def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len(digits) == 0:
        return [0]
    return decimal_to_output_base(input_base_to_decimal(input_base, digits), output_base)
