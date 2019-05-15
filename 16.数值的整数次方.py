from exeTime import exeTime


@exeTime
def Power(base, exponent):
    if not exponent: return 1
    if not base and exponent < 0: return None
    if exponent == 1: return base
    res = base
    n = 2
    while n <= abs(exponent):
        res = base * res
        n += 1
    if exponent > 0: return res
    else: return 1 / res


@exeTime
def Power2(base, exponent):
    return base**exponent


if __name__ == "__main__":
    base = 2.369
    exponent = 10
    print(Power(base, exponent))
    print(Power2(base, exponent))
