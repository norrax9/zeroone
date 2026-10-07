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