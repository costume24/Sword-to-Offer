from exeTime import exeTime
from multitimes import multitimes


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    @multitimes
    def FindNumsAppearOnce(self, array):
        '''使用异或运算
        所有的数字进行异或，得到的是只出现一次的两个数字的异或结果
        该结果必至少有一位为1
        按照该位是否为1将数组分为两部分
        每个部分仅包含一个出现一次的数字
        对这两个部分进行异或即可得到
        '''
        if not array: return []
        all_xor = 0
        for item in array:
            all_xor = all_xor ^ item
        xor_list = list(bin(all_xor))
        index = -1
        for i in range(len(xor_list)):
            if xor_list[-i] == '1':
                index = -i
        bin_xor = list(map(bin, array))
        a, b = 0, 0
        for item in bin_xor:
            if item[index] == '0':
                a = a ^ int(item, 2)
            else:
                b = b ^ int(item, 2)
        return [a, b]

    @multitimes
    def FindNumsAppearOnce2(self, array):
        # write code here
        d = {}
        ls = []
        for i in array:
            d[i] = d.get(i, 0) + 1
        for j in d:
            if d[j] == 1:
                ls.append(j)
            if len(ls) == 2:
                break
        return ls


if __name__ == "__main__":
    so = Solution()
    array = [1, 3, 2, 2, 4, 5, 3, 1, 6, 7, 8, 9, 8, 7, 9, 6]
    print(so.FindNumsAppearOnce(array))
    print(so.FindNumsAppearOnce2(array))
