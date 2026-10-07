from methods import (
    toDigitsArray,
    toTwosComplement,
    addTwosComplement,
    fromTwosComplement,
    arrayToInt,
)

if __name__ == "__main__":
    print("toDigitsArray(10):", toDigitsArray(10))

    a = toTwosComplement(5)
    b = toTwosComplement(-3)
    print("5 в доп. коде:", a)
    print("-3 в доп. коде:", b)

    s = addTwosComplement(a, b)
    print("5 + (-3) в доп. коде:", s)
    print("в прямом коде:", fromTwosComplement(s))
    print("arrayToInt(s):", arrayToInt(s))

    neg = toTwosComplement(-5)
    print("-5 в доп. коде:", neg)
    print("-5 в прямом коде:", fromTwosComplement(neg))
