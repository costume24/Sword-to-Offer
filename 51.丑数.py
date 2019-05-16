from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    @exeTime
    def GetUglyNumber_Solution(self, index):
        '''
        用一个排序的数组保存已找到的丑数
        新的丑数由前面的丑数各自乘上2,3,5的最小值得到
        由于是排好序的，因此存在位置t2，使得在t2之前的数字乘22仍然小于当前最大的丑数，
        在t2之后（包括t2）乘2大于最大的丑数，故实际上只需要计算2*t2即可
        对于t3，t5同理
        更新时，只看新的丑数包不包含2,3,5，包含的话对应的位置前进一位即可
        '''
        if index < 1: return 0
        res = [1, 2, 3, 4, 5]
        t2 = 2
        t3 = 1
        t5 = 1
        for i in range(5, index + 1):
            m2 = 2 * res[t2]
            m3 = 3 * res[t3]
            m5 = 5 * res[t5]
            res.append(min(m2, m3, m5))
            while 2 * res[t2] <= res[-1]:
                t2 += 1
            while 3 * res[t3] <= res[-1]:
                t3 += 1
            while 5 * res[t5] <= res[-1]:
                t5 += 1
        return res[index - 1]

    @exeTime
    def GetUglyNumber_Solution2(self, index):
        # write code here
        if index < 1: return 0
        res = [1, 2, 3, 4, 5]
        t2 = 2
        t3 = 1
        t5 = 1
        for i in range(5, index + 1):
            m2 = 2 * res[t2]
            m3 = 3 * res[t3]
            m5 = 5 * res[t5]
            res.append(min(m2, m3, m5))
            if res[-1] % 2 == 0:
                t2 += 1
            if res[-1] % 3 == 0:
                t3 += 1
            if res[-1] % 5 == 0:
                t5 += 1
        return res[index - 1]


if __name__ == "__main__":
    so = Solution()
    index = 9999
    print(so.GetUglyNumber_Solution(index))
    print(so.GetUglyNumber_Solution2(index))
