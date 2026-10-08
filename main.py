from methods import (
    toTwosComplement,
    addTwosComplement,
    fromTwosComplement,
    arrayToInt,
)

BITS = 16


def toStr(arr):
    return ''.join(map(str, arr))


if __name__ == '__main__':
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))

    a = toTwosComplement(x, BITS)
    b = toTwosComplement(y, BITS)
    print(f'{x} в доп. коде: {toStr(a)}')
    print(f'{y} в доп. коде: {toStr(b)}')

    try:
        s = addTwosComplement(a, b)
    except OverflowError:
        print('Переполнение: сумма не помещается в', BITS, 'бит')
    else:
        direct = fromTwosComplement(s)
        sign = -1 if direct[0] == 1 else 1
        value = sign * arrayToInt(direct[1:])
        print(f'Сумма в доп. коде: {toStr(s)}')
        print(f'Сумма в прямом коде: {toStr(direct)}')
        print(f'Сумма в десятичной: {value}')
