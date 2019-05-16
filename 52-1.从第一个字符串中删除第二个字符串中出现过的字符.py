from exeTime import exeTime


class Solution:
    @exeTime
    def deleteCharInSecondStringFromFirstString(self, s1, s2):
        if not s1: return None
        if not s2: return s1
        ignore = []
        s2 = list(s2)
        for i in range(len(s1)):
            if s1[i] in s2:
                ignore.append(i)
        res = ''
        for i in range(len(s1)):
            if i not in ignore:
                res += s1[i]
        return res


if __name__ == "__main__":
    so = Solution()
    s1 = 'We are students'
    s2 = 'aeiou'
    print(so.deleteCharInSecondStringFromFirstString(s1, s2))
