
def num_to_two():
    num = int(input("Введите число: "))
    s = ""
    temp = abs(num)
    
    while temp > 0:
        s = str(temp % 2) + s
        temp //= 2
        
    bits = [int(char) for char in s]
    
    if len(bits) < 16:
        bits = [0] * (16 - len(bits)) + bits
    else:
        bits = bits[-16:] 
        
    return bits

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

