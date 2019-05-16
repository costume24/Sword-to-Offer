from exeTime import exeTime


class Solution:
    @exeTime
    def delRepeatedChars(self, s):
        if not s: return
        hasShown = {}
        ignore = []
        for i in range(len(s)):
            if s[i] not in hasShown.keys():
                hasShown[s[i]] = 1
            else:
                ignore.append(i)
        res = ''
        for i in range(len(s)):
            if i not in ignore:
                res += s[i]
        return res


if __name__ == "__main__":
    so = Solution()
    s = 'occrualsdjfkla;sjdlahsdlknflsd;jfaskjweuroiytbmnznweot[awmx,vwspfjxnx,a[qwjfj;kslm'
    print(so.delRepeatedChars(s))
