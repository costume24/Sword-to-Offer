from exeTime import exeTime
from functools import reduce
import itertools


class Solution:
    @exeTime
    def Combination1(self, ss):
        '''利用二进制

        若字符串长度为3，对于每一位上的字符，都可以选或者不选
        恰好对应8个二进制数，每一位为0表示不选，为1表示选
        '''
        if not ss: return []
        s = list(ss)
        res = []
        binList = []
        for i in range(2**len(s)):
            binList.append(bin(i)[2:])
            if i < 4:
                compliment = len(s) - len(binList[i])
                binList[i] = '0' * compliment + binList[i]
        for item in binList:
            tmp = ''
            for i in range(len(item)):
                if item[i] == '1':
                    tmp += s[i]
            res.append(tmp)
        return sorted(res[1:])

    @exeTime
    def Combination2(self, ss):
        '''递归解法

        假设字符串长度为n，则所有组合的长度为m，取值区间为[0,n]
        对于每个长度m，从头扫描字符串，每一位都可以选或者不选
        若选，则在剩余的n-1位中选取m-1个
        若不选，则在剩余的n-1位中选取m个
        '''
        if not ss: return None
        res = []
        now = ''
        start = 0
        for nums in range(1, len(ss)):
            self.do(ss, res, start, nums, now)
        return list(set(res))

    def do(self, ss, res, start, nums, now):
        if nums == 0:
            res.append(now)
            return res
        s = ss[:]
        for i in range(start, len(s)):
            self.do(ss, res, i + 1, nums, now)  # 不选
            now += s[i]
            self.do(ss, res, i + 1, nums - 1, now)  # 选
        return res

    @exeTime
    def Combination3(self, ss):
        '''使用Python自带的itertools，速度最快
        '''
        s = list(ss)
        res = []
        for i in range(len(s)):
            res.append(
                sorted(list(set(map(''.join, itertools.combinations(s, i))))))
        tmp = []
        for i in range(len(res)):
            if res[i][0] == '':
                res[i][0] = ss
            tmp.extend(res[i])

        return tmp


if __name__ == "__main__":
    so = Solution()
    ss = 'abc'
    res = so.Combination1(ss)
    print(res)
    res = so.Combination2(ss)
    print(res)

    res = so.Combination3(ss)
    print(res)
