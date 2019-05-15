from exeTime import exeTime
import numpy as np
'''另一种复杂度为O(nlogk)的方法，特别适合处理海量数据。
用一个大小为k的容器来存储最小的k个容器
每次读入一个数
    若容器未满，则放入
    若容器已满，此时若该数小于容器里的最大值，则放入
由于每次都要求最大值，所以用最小堆或红黑树
'''


class Solution:
    @exeTime
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return None
        lyst = sorted(tinput)
        return lyst[:k]

    @exeTime
    def GetLeastNumbers_Solution2(self, tinput, k):
        if not tinput or len(tinput) < k or not k:
            return None
        start = 0
        end = len(tinput)
        index = self.partion(tinput, start, end)
        while index != k - 1:
            if index < k - 1:
                index = self.partion(tinput, index + 1, end)
            elif index > k - 1:
                index = self.partion(tinput, start, index)
        return tinput[:index + 1]

    def partion(self, num, start, end):
        pivot = num[end - 1]
        p = start - 1
        for i in range(start, end - 1):
            if num[i] <= pivot:
                p += 1
                num[i], num[p] = num[p], num[i]
        num[p + 1], num[end - 1] = num[end - 1], num[p + 1]
        return p + 1


if __name__ == "__main__":
    so = Solution()
    tinput = list(np.random.randint(0, 500, 400))
    tmp = tinput[:]
    k = 4
    print(so.GetLeastNumbers_Solution(tinput, k))
    print(so.GetLeastNumbers_Solution2(tmp, k))
