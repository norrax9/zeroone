def toDigitsArray(n):
    """Перевод целого числа из десятичной системы счисления в двоичную.

    Возвращает массив цифр (старший разряд первым) для модуля числа.
    Пример: toDigitsArray(10) -> [1, 0, 1, 0]
    """
    n = abs(int(n))
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 2)
        n //= 2
    digits.reverse()
    return digits
