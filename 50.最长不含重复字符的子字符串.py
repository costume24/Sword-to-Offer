from exeTime import exeTime


class Solution:
    def longestSubstringWithoutDuplication(self, s):
        '''动态规划解法
        两个辅助数组：
            longest:记录以第i个字符结尾的最长不重复子串
            lastIndex:记录第i个字符上次出现的位置（字典）
        1、若字符之前没有出现过，则longest[i]=longest[i-1]+1
        2、若之前出现过，计算与当前位置的距离d：
            （1）d<=longest[i-1]:说明出现重复，则longest[i]=d
            （2）d>longest[i-1]:说明无重复，则按情况1处理
        '''
        if not s: return ''
        slen = len(s)
        longest = [0 for i in range(slen)]
        lastIndex = {char: -1 for char in s}
        for i in range(slen):
            if i == 0:
                longest[i] = 1
            else:
                if lastIndex[s[i]] == -1:
                    longest[i] = longest[i - 1] + 1
                else:
                    d = i - lastIndex[s[i]]
                    if d > longest[i - 1]:
                        longest[i] = longest[i - 1] + 1
                    else:
                        longest[i] = d
            lastIndex[s[i]] = i
        maxLen = max(longest)
        maxIndex = longest.index(maxLen)
        return s[maxIndex - maxLen + 1:maxLen + 1]


if __name__ == "__main__":
    so = Solution()
    s = 'arabcacrf'
    print(so.longestSubstringWithoutDuplication(s))
