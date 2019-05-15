from exeTime import exeTime
'''python的整型没有溢出。转化为二进制时，负数前面会用一个负号表示。
题目要求负数用补码表示，因此需要与上全1的二进制数，对于32位来说，就是0xffffffff。
'''


@exeTime
def NumberOf1(n):
    '''整数减去1后与原来的整数做按位与运算，得到的结果相当于把整数的二进制
    表示中最右边的1变为0。
    '''
    count = 0
    if n < 0:
        n = n & 0xFFFFFFFF
    while n:
        count += 1
        n = n & (n - 1)
    return count


@exeTime
def NumberOf1II(n):
    if n < 0:
        n = n & 0xffffffff
    return sum(map(int, list(bin(n))[2:]))


if __name__ == "__main__":
    n = -2147483648
    print(NumberOf1(n))
    print(NumberOf1II(n))
