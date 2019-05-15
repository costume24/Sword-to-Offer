from exeTime import exeTime


class Solution:
    def transNumToStr(self, num):
        '''动态规划式子为：
        f(i)=f(i+1)+g(i,i+1)*f(i+2)
        g(i,i+1)判断两个字符是否可以用一个字母表示
        '''
        now, neg1, neg2 = 0, 0, 0
        num = str(num)
        if len(num) == 1: return 1
        elif len(num) == 2: return 2 if '9' < num < '26' else 1
        for i in range(len(num) - 1, -1, -1):
            if i == len(num) - 1:
                now = 1
                neg1 = now
            elif i == len(num) - 2:
                now = neg1 + self.judge(num[i], num[i + 1])
                neg2 = neg1
                neg1 = now
            else:
                now = neg1 + self.judge(num[i], num[i + 1]) * neg2
                neg2 = neg1
                neg1 = now
        return now

    def judge(self, a, b):
        t = a + b
        return 1 if '09' < a + b < '26' else 0


if __name__ == "__main__":
    so = Solution()
    num = 12258135874125478
    print(so.transNumToStr(num))
