from exeTime import exeTime
from multitimes import multitimes


class Solution:
    @multitimes
    def FindNumbersWithSum(self, array, tsum):
        '''优化的遍历法
        找到第一个比tsum小的数作为起点，找到第一个比tsum的一半大的数作为终点
        在起点和终点之间，依次寻找
        '''
        if not array: return
        res = []
        index = 0
        if tsum < array[-1]:
            index = self.bin_search(array, tsum, 0, len(array))
        else:
            index = len(array) - 1
        stop = int(tsum / 2)
        stop_index = self.bin_search(array, stop, 0, index)
        for i in range(stop_index, index + 1):
            diff = tsum - array[i]
            if diff in array[:index]:
                res.append([array[i], diff])

        product = list(map(lambda x: x[0] * x[1], res))
        return sorted(res[product.index(min(product))])

    def bin_search(self, array, aim, start, end):
        if start >= end: return start
        mid = int((end + start) / 2)
        index = 0
        if array[mid] < aim:
            index = self.bin_search(array, aim, mid + 1, end)
        elif array[mid] >= aim:
            index = self.bin_search(array, aim, start, mid - 1)
        else:
            return mid
        return index

    @multitimes
    def FindNumbersWithSum2(self, array, tsum):
        '''双指针法
        一个指向头，一个指向尾
        若和小于tsum，则头后移
        若和大于tsum，则尾前移
        '''
        if not array: return []
        head = 0
        tail = len(array) - 1
        res = []
        while head <= tail:
            sum_now = array[head] + array[tail]
            if sum_now == tsum:
                res.append([array[head], array[tail]])
                head += 1
            elif sum_now < tsum:
                head += 1
            else:
                tail -= 1
        if not res: return []
        product_list = list(map(lambda x: x[0] * x[1], res))
        return sorted(res[product_list.index(min(product_list))])


if __name__ == "__main__":
    so = Solution()
    array = [1, 2, 4, 7, 11, 16]
    tsum = 15
    print(so.FindNumbersWithSum(array, tsum))
    print(so.FindNumbersWithSum2(array, tsum))
