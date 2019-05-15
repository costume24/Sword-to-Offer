from exeTime import exeTime


class Solution:
    @exeTime
    def match(self, s, pattern):
        if not s and not pattern: return True  # 都为空，返回True
        if not pattern: return False  # 模式为空，返回False
        n, m = len(s), len(pattern)
        if n == 0:  # 文本为空，也可能匹配成功
            if pattern[-1] != '*': return False
            k = 0
            while k < m - 1:
                if pattern[k] == '.' and pattern[k + 1] != '*': return False
                k += 1
            return True
        i, j = 0, 0
        return self.matchCore(i, j, n, m, s, pattern)

    def matchCore(self, i, j, n, m, s, pattern):
        if i == n - 1 and j == m - 1:
            if s[i] == pattern[j] or pattern[j] == '.': return True
            return False
        if i == n and j == m: return True
        if i == n and j < m:
            if '.' in pattern[j:-1] or pattern[j] == '.': return False
            if pattern[-1] != '*': return False
            for j in range(j, m - 1):
                if pattern[j] != '*':
                    if pattern[j + 1] != '*': return False
            return True
        if j >= m: return False
        if s[i] == pattern[j] or pattern[j] == '.':
            if pattern[j + 1] == '*':
                # 下一位为'*'，有三种情况
                # 可以匹配多个
                # 可以匹配一个
                # 可以匹配0个
                # a = self.matchCore(i + 1, j, n, m, s, pattern)
                # b = self.matchCore(i + 1, j + 2, n, m, s, pattern)
                # c = self.matchCore(i, j + 2, n, m, s, pattern)
                return self.matchCore(i+1,j,n,m,s,pattern) \
                    or self.matchCore(i+1,j+2,n,m,s,pattern) \
                        or self.matchCore(i,j+2,n,m,s,pattern)
            else:
                return self.matchCore(i + 1, j + 1, n, m, s, pattern)
        return False

    @exeTime
    def match2(self, s, pattern):
        # write code here
        if (len(s) == 0 and len(pattern) == 0):
            return True
        if (len(s) > 0 and len(pattern) == 0):
            return False
        if (len(pattern) > 1 and pattern[1] == '*'):
            if (len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.')):
                return (self.match2(s, pattern[2:])
                        or self.match2(s[1:], pattern[2:])
                        or self.match2(s[1:], pattern))
            else:
                return self.match2(s, pattern[2:])
        if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
            return self.match2(s[1:], pattern[1:])
        return False


if __name__ == "__main__":
    so = Solution()
    s = ''
    pattern = 'ab*'
    print(so.match2(s, pattern))
    print(so.match(s, pattern))
