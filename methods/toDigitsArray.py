def toDigitsArray(n):
    n = abs(int(n))
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 2)
        n //= 2
    digits.reverse()
    return digits
