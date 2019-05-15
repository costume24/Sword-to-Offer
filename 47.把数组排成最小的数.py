from exeTime import exeTime
'''O(n!)解法：全排列再求最小的
'''

# -*- coding:utf-8 -*-
import functools


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ''
        numbers = list(map(str, numbers))
        numbers = sorted(numbers, key=functools.cmp_to_key(self.compare))
        s = ''
        for item in numbers:
            s += item
        return s

    def compare(self, i, j):
        comb1 = i + j
        comb2 = j + i
        if comb1 > comb2:
            return 1
        elif comb1 <= comb2:
            return -1
        else:
            return 0


if __name__ == "__main__":
    so = Solution()
    number = [3, 32, 321]
    print(so.PrintMinNumber(number))
