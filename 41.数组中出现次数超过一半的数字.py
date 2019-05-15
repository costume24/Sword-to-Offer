from exeTime import exeTime
import numpy as np


class Solution:
    @exeTime
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers: return None
        nlen = len(numbers)
        if nlen == 1: return numbers[0]
        stat = {}
        for item in numbers:
            if item not in stat.keys():
                stat[item] = 1
            stat[item] += 1
            if stat[item] > nlen / 2: return item
        return 0

    @exeTime
    def MoreThanHalfNum_Solution2(self, numbers):
        '''出现次数超过一半的数字，其出现次数比其他所有数字出现次数之和还要大

        因此每出现一个其他数字，就抵消一次
        此方法可能会出现问题
        如输入为[2, 2, 4, 4, 1, 4, 2, 4, 4]时，有两个4用于抵消一开始的2
        因此最终4的计数个数没有超过一半
        '''
        if not numbers: return None
        nlen = len(numbers)

        if nlen == 1: return numbers[0]
        res = numbers[0]
        times = 1
        for item in numbers:
            if times == 0:
                res = item
                times = 1
            elif res == item:
                times += 1
            elif res != item:
                times -= 1
        return res if res > (nlen / 2) else 0

    @exeTime
    def MoreThanHalfNum_Solution3(self, numbers):
        '''在排序后的数组中，出现次数超过一半的数字一定是在数组中间的数字，即中位数

        中位数即排序数组中第n/2大的数，有一种O(n)时间内找出第k大数字的方法，这种算法受随机快排的启发。
        先随机选择一个数字，将比它小的移到左边，大的移到右边。
        最终其下标若正好为n/2，则就是要找的数字；若小于，则找其右边的；若大于，则找其左边的
        '''
        if not numbers: return []
        mid = int((len(numbers) / 2))
        start = 0
        end = len(numbers)
        index = self.partion(numbers, start, end)
        while index != mid:
            if index < mid:
                index = self.partion(numbers, index + 1, end)
            elif index > mid:
                index = self.partion(numbers, start, index)
        if self.check(numbers, numbers[index]):
            return numbers[index]
        return 0

    def partion(self, num, start, end):
        pivot = num[end - 1]  # 选择主元
        p = start - 1  # 边界指针
        for i in range(start, end - 1):
            if num[i] <= pivot:  #将小于主元的移到边界左边
                p += 1
                num[i], num[p] = num[p], num[i]
        num[p + 1], num[end - 1] = num[end - 1], num[p + 1]  # 最后将主元放到正确的位置上
        return p + 1

    def check(self, num, aim):
        count = 0
        for item in num:
            if item == aim: count += 1
        return True if count > len(num) / 2 else False


if __name__ == "__main__":
    so = Solution()
    s = [7] * 502
    s.extend(list(range(500)))
    np.random.shuffle(s)
    print(so.MoreThanHalfNum_Solution(s))
    print(so.MoreThanHalfNum_Solution2(s))
    print(so.MoreThanHalfNum_Solution3(s))
