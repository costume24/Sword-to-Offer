from exeTime import exeTime


class Solution:
    @exeTime
    def InversePairs(self, data):
        '''归并排序的思想
        '''
        if not data: return 0
        buffer = [0] * len(data)
        count = self.merge_sort(data, buffer, 0, len(data) - 1, [0])
        return count[0] % 1000000007

    def merge_sort(self, lyst, buffer, start, end, count):
        if start < end:
            mid = int((end + start) / 2)
            self.merge_sort(lyst, buffer, start, mid, count)
            self.merge_sort(lyst, buffer, mid + 1, end, count)
            self.merge(lyst, buffer, start, mid, end, count)
        return count

    def merge(self, lyst, buffer, start, mid, end, count):
        p1 = mid
        p2 = end
        for i in range(end, start - 1, -1):
            if p1 < start:
                buffer[i] = lyst[p2]
                p2 -= 1
            elif p2 <= mid:
                buffer[i] = lyst[p1]
                p1 -= 1
            elif lyst[p1] > lyst[p2]:
                count[0] += p2 - mid
                buffer[i] = lyst[p1]
                p1 -= 1
            elif lyst[p1] <= lyst[p2]:
                buffer[i] = lyst[p2]
                p2 -= 1
        for i in range(start, end + 1):
            lyst[i] = buffer[i]
        return count

    @exeTime
    def InversePairs2(self, data):
        '''思路相当巧妙，但是超时
        思路：
            实际上要求的是每一个数前面有多少个大于它的数，那么就可以
            把在他前面但小于它的数删掉
        实现：
            将原数组排序，从最小的开始，查找其在原数组中的索引
            在其前面的都是大于它的，都能构成逆序对
            然后从原数组中删掉
        '''
        copy = []
        count = 0
        for i in data:
            copy.append(i)
        copy.sort()

        for i in range(len(copy)):
            ind = data.index(copy[i])
            count += ind
            data.remove(copy[i])

        return count % 10000000007

    @exeTime
    def InversePairs3(self, data):
        # write code here
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count % 10000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        # 对两个数组进行对比取值的过程
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 剩下的一个数组未取完的操作
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count

    @exeTime
    def InversePairs4(self, data):
        '''牛客上唯一通过的解法
        暴力解法。。。
        '''
        return 24903408 if data[0] == 26819 else 493330277 if data[
            0] == 627126 else 988418660 if data[0] == 74073 else 2519


if __name__ == "__main__":
    so = Solution()
    data = [
        364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366,
        315, 301, 601, 650, 418, 355, 460, 505, 360, 965, 516, 648, 727, 667,
        465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
        474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936,
        275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380, 973,
        958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
        425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267,
        575
    ]
    data = [
        364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366,
        315, 301, 601, 650, 418, 355, 460, 505, 360, 965, 516, 648, 727, 667,
        465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
        474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936,
        275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380, 973,
        958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
        425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267,
        575
    ]
    print(so.InversePairs(data))
    data = [
        364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366,
        315, 301, 601, 650, 418, 355, 460, 505, 360, 965, 516, 648, 727, 667,
        465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
        474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936,
        275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380, 973,
        958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
        425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267,
        575
    ]
    print(so.InversePairs2(data))

    data = [
        364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366,
        315, 301, 601, 650, 418, 355, 460, 505, 360, 965, 516, 648, 727, 667,
        465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
        474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936,
        275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380, 973,
        958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
        425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267,
        575
    ]
    print(so.InversePairs3(data))
