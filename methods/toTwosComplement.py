def binary_to_decimal(binary_str):
    decimal_val = 0
    for index, digit in enumerate(reversed(binary_str)):
        if digit == "1":
            decimal_val += 2 ** index
    return decimal_val



