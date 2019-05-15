from exeTime import exeTime

from numpy import math


# -*- coding:utf-8 -*-
class Solution:
    @exeTime
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n: return 0
        count = 0
        for i in range(1, n + 1):
            tmp = str(i)
            for item in tmp:
                if item == '1':
                    count += 1
        return count

    def NumberOf1Between1AndN_Solution2(self, n):
        if not n: return 0
        numLen = len(str(n))
        count = 0
        for i in range(1, numLen + 1):
            for j in range(1, i + 1):
                count += 9**(i - j) * self.combination(i, j)
        return count

    def combination(self, n, m):
        if n == m: return 1
        return math.factorial(n) / (math.factorial(n - m) * math.factorial(m))


if __name__ == "__main__":
    so = Solution()
    n = 20
    print(so.NumberOf1Between1AndN_Solution(n))
    print(so.NumberOf1Between1AndN_Solution2(n))
