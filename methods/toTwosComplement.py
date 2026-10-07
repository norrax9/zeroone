

from toDigitsArray import num_to_two


def to_twos_complement():
    bits = num_to_two()
    
    inverted = [1 if bit == 0 else 0 for bit in bits]
    
    carry = 1
    for i in range(len(inverted) - 1, -1, -1):
        total = inverted[i] + carry
        if total == 2:
            inverted[i] = 0
            carry = 1
        else:
            inverted[i] = total
            carry = 0
            break
            
    return inverted

if __name__ == "__main__":
    print("16-битный дополнительный код:", to_twos_complement())
def binary_to_decimal(binary_str):
    decimal_val = 0
    for index, digit in enumerate(reversed(binary_str)):
        if digit == "1":
            decimal_val += 2 ** index
    return decimal_val





def fromTwosComplement(arr):
    arr = list(arr)
    if arr[0] == 0:
        return arr

    magnitude = [1 - d for d in arr[1:]]
    carry = 1
    for i in range(len(magnitude) - 1, -1, -1):
        total = magnitude[i] + carry
        magnitude[i] = total % 2
        carry = total // 2
    if carry:
        raise OverflowError("Наименьшее число нельзя представить в прямом коде")
    return [1] + magnitude
