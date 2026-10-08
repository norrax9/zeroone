def _extend(arr, length):
    return [arr[0]] * (length - len(arr)) + list(arr)


def addTwosComplement(a, b):
    length = max(len(a), len(b))
    a = _extend(a, length)
    b = _extend(b, length)
    result = [0] * length
    carry = 0
    for i in range(length - 1, -1, -1):
        total = a[i] + b[i] + carry
        result[i] = total % 2
        carry = total // 2
    if a[0] == b[0] and result[0] != a[0]:
        raise OverflowError('Переполнение при сложении')
    return result
