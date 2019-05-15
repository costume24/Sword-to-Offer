from exeTime import exeTime


@exeTime
def jumpFloorII(number):
    """一次可以跳1-n阶台阶
    所以需要保存前面n-1次的记录，第n次等于前面n-1次的和再加1（一次跳n阶）
    """
    if number == 1:
        return 1
    if number == 2:
        return 2
    nums = [1, 2]
    res = 3
    for _ in range(3, number + 1):
        res = sum(nums) + 1
        nums.append(res)
    return res


@exeTime
def jumpFloorII2(number):
    """数学归纳法可知，此时第n次为2**(n-1)
    """
    return 2 ** (number - 1)


if __name__ == "__main__":
    number = 50
    print(jumpFloorII(number))
    print(jumpFloorII2(number))
