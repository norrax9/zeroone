def NumToTwo():
    num = int(input("Введите число:"))
    if num == 0:
        return 0
    s = []
    while num > 0:
        s.append(num % 2)
        num //= 2

    return s