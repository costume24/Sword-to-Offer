from exeTime import exeTime
from functools import reduce


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss: return []
        s = list(ss)
        res = []
        self.do(s, res, 0)
        res = list(set(res))  # 去重
        return sorted(res)  # 按首字母排序

    def do(self, ss, res, start):
        s = ss[:]
        if start == len(s) - 1:
            s = str(reduce(lambda x, y: x + y, s))  # 将s转化为字符串
            res.append(s)
            return res
        for i in range(start, len(s)):
            if s[i] != s[start]:
                s[i], s[start] = s[start], s[i]
            self.do(s, res, start + 1)
        return res


if __name__ == "__main__":
    so = Solution()
    ss = 'aab'
    res = so.Permutation(ss)
    for s in res:
        print(s)