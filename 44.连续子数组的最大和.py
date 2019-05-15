from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 1: return array[0]
        start, end, sumNow, sumMax = 0, 0, 0, -65565
        for i in range(len(array)):
            if sumNow + array[i] < array[i]:
                start = i
                sumNow = array[i]

            else:
                sumNow += array[i]
            if sumNow > sumMax:
                sumMax = sumNow
            else:
                end = i

        return start, end, sumMax


if __name__ == "__main__":
    so = Solution()
    array = [-2, -8, -1, -6]
    start, end, sumMax = so.FindGreatestSumOfSubArray(array)
    print(array[start:end])
    print(sumMax)
