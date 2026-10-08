def _extend(arr, length):
    """Расширение знаковым битом до нужной длины."""
    return [arr[0]] * (length - len(arr)) + list(arr)


def addTwosComplement(a, b):
    """Сложение двух чисел, заданных массивами в дополнительном коде.

    Если длины разные, короткое число расширяется знаковым битом.
    Перенос из старшего разряда отбрасывается.
    При переполнении выбрасывается OverflowError.
    Пример: [0,0,0,0,0,1,0,1] + [1,1,1,1,1,1,0,1] (5 + -3) -> [0,0,0,0,0,0,1,0]
    """
    length = max(len(a), len(b))
    a = _extend(a, length)
    b = _extend(b, length)

    result = [0] * length
    carry = 0
    for i in range(length - 1, -1, -1):
        total = a[i] + b[i] + carry
        result[i] = total % 2
        carry = total // 2

    # Переполнение: знаки слагаемых одинаковые, а знак результата другой
    if a[0] == b[0] and result[0] != a[0]:
        raise OverflowError("Переполнение при сложении")
    return result
