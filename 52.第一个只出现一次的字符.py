from exeTime import exeTime
import string


class Solution:
    @exeTime
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s: return -1
        res = {}
        for i in range(65, 91):
            res[chr(i)] = [0, -1]
        for i in range(97, 123):
            res[chr(i)] = [0, -1]
        for i in range(len(s)):
            res[s[i]][0] += 1
            if res[s[i]][1] == -1:
                res[s[i]][1] = i
        tmp = [v[1] for k, v in res.items() if v[0] == 1]

        return min(tmp) if tmp else -1

    @exeTime
    def FirstNotRepeatingChar2(self, s):
        '''扫描两次，第一次得到次数
        第二次找到第一个次数为1的字符的位置
        '''
        if not s: return -1
        res = {}
        for char in s:
            if char not in res.keys():
                res[char] = 0
            res[char] += 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1

    @exeTime
    def FirstNotRepeatingChar3(self, s):
        # write code here
        if not s: return -1
        res = {}
        for key in string.ascii_letters:
            res[key] = [0, -1]
        for i in range(len(s)):
            res[s[i]][0] += 1
            if res[s[i]][1] == -1:
                res[s[i]][1] = i
        tmp = [v[1] for k, v in res.items() if v[0] == 1]

        return min(tmp) if tmp else -1


if __name__ == "__main__":
    so = Solution()
    s = 'gooadfdfadfdcdasdfsderetgasergbadfwerfadcxdfawqewrdfasdgle'
    print(so.FirstNotRepeatingChar(s))
    print(so.FirstNotRepeatingChar2(s))
    print(so.FirstNotRepeatingChar3(s))
