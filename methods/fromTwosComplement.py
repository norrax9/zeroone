def fromTwosComplement(arr):
    """Перевод из дополнительного кода в прямой.

    Положительные числа (знаковый бит 0) остаются без изменений.
    У отрицательных знаковый бит сохраняется, остальные разряды
    инвертируются, и к ним прибавляется 1.
    Пример: [1,1,1,1,1,0,1,1] (-5) -> [1,0,0,0,0,1,0,1]
    """
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
