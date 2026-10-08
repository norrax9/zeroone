from .toDigitsArray import toDigitsArray


def toTwosComplement(n, bits=8):
    """Перевод целого числа в дополнительный код длиной bits разрядов.

    Возвращает массив битов (старший разряд - знаковый).
    Примеры:
        toTwosComplement(5, 8)  -> [0, 0, 0, 0, 0, 1, 0, 1]
        toTwosComplement(-5, 8) -> [1, 1, 1, 1, 1, 0, 1, 1]
    """
    n = int(n)
    low = -(2 ** (bits - 1))
    high = 2 ** (bits - 1) - 1
    if n < low or n > high:
        raise ValueError(f"Число {n} не помещается в {bits} бит ({low}..{high})")

    if n >= 0:
        digits = toDigitsArray(n)
        return [0] * (bits - len(digits)) + digits

    # Отрицательное: инвертируем модуль и прибавляем 1
    digits = toDigitsArray(-n)
    result = [0] * (bits - len(digits)) + digits
    result = [1 - d for d in result]
    carry = 1
    for i in range(bits - 1, -1, -1):
        total = result[i] + carry
        result[i] = total % 2
        carry = total // 2
    return result
