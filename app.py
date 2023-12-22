def factorial(num):
    res = 1
    iter = num
    while (num != 0):
        res *= num
        num -= 1
    return res