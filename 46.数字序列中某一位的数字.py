from exeTime import exeTime


class Solution:
    def digitAtIndex(self, index):
        if index < 0:
            return -1
        digits = 1
        number = 0
        while True:
            number = self.countOfIntegers(digits)
            if index < number * digits:
                return self.findIndex(index, digits)
            index -= digits * number
            digits += 1
        return -1

    def countOfIntegers(self, digits):
        '''计算m位数字的个数
        '''
        if digits == 1:
            return 10
        count = 10**(digits - 1)
        return 9 * count

    def beginNumber(self, digits):
        if digits == 1:
            return 0
        return 10**(digits - 1)

    def findIndex(self, index, digits):
        number = self.beginNumber(digits) + int(index / digits)
        indexFromRight = digits - index % digits
        for i in range(1, indexFromRight):
            number /= 10
        return int(number % 10)


if __name__ == "__main__":
    so = Solution()
    index = 19
    print(so.digitAtIndex(index))