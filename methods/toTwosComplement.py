from toDigitsArray import NumToTwo


def to_twos_complement():
    bits = NumToTwo()

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

    # Если после сложения остался перенос (выход за разрядность), можно его учесть
    if carry == 1:
        inverted.insert(0, 1)

    return inverted


if __name__ == "__main__":
    print("Дополнительный код:", to_twos_complement())