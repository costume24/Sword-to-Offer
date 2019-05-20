from exeTime import exeTime


class Solution:
    @exeTime
    def GetNumberOfK(self, data, k):
        '''Python特色解法
        找到数字第一次出现的索引，和原数组中该数字后的一个数字索引
        '''
        if not data or not k in data: return 0
        f1 = data.index(k)
        max_num = max(data)
        diff = max_num - k
        if diff == 0:
            return len(data) - f1
        for i in range(1, diff + 1):
            if k + i in data:
                f2 = data.index(k + i)
                return f2 - f1

    @exeTime
    def GetNumberOfK2(self, data, k):
        '''二分法的思想
        找到第一次出现：
            如果中间数字等于k，则判断前一位是否为k
        找到最后一次出现：
            如果中间数字等于k，则判断后一位是否为k
        '''
        if not data: return -1
        num = 0
        length = len(data)
        first = self.getfirst(data, length, k, 0, length - 1)
        last = self.getlast(data, length, k, 0, length - 1)
        if first > -1 and last > -1:
            num = last - first + 1
        return num

    def getfirst(self, data, length, k, start, end):
        '''找到第一次出现：
            如果中间数字等于k，则判断前一位是否为k
        '''
        if start > end:
            return -1
        mid = int((start + end) / 2)
        mid_element = data[mid]
        if mid_element == k:
            if (mid > 0 and data[mid - 1] != k) or mid == 0:
                return mid
            else:
                end = mid - 1
        elif mid_element > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.getfirst(data, length, k, start, end)

    def getlast(self, data, length, k, start, end):
        '''找到最后一次出现：
            如果中间数字等于k，则判断后一位是否为k
        '''
        if start > end:
            return -1
        mid = int((start + end) / 2)
        mid_element = data[mid]
        if mid_element == k:
            if (mid < length - 1 and data[mid + 1] != k) or mid == length - 1:
                return mid
            else:
                start = mid + 1
        elif mid_element < k:
            start = mid + 1
        else:
            end = mid - 1
        return self.getlast(data, length, k, start, end)


if __name__ == "__main__":
    so = Solution()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    print(so.GetNumberOfK(data, k))
    print(so.GetNumberOfK2(data, k))
