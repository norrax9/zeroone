def arrayToInt(arr):
    """Перевод из двоичной системы счисления (массив цифр) в десятичную.

    Старший разряд первым.
    Пример: arrayToInt([1, 0, 1, 0]) -> 10
    """
    result = 0
    for d in arr:
        result = result * 2 + d
    return result
