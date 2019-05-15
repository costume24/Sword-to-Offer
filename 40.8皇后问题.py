from exeTime import exeTime
from functools import reduce
import itertools


class Solution:
    @exeTime
    def queen8(self):
        '''使用全排列解决八皇后问题

        数组cols中第i个元素代表第i行的皇后所处的列号
        这8个数字肯定是各不相同的（不能在同一列）
        放置在8行，则肯定不在同一行
        因此只需要求出8个数字的全排列，对每个排列判断是否有同斜线的皇后即可
        判断条件：|i-j|==|vec[i]-vec[j]|
        打开绝对值则有：
                i-vec[i]==j-vec[j]
                i+vec[i]==j+vec[j]
        '''
        cols = range(8)
        res = []
        for vec in itertools.permutations(cols):
            if (8 == len(set(vec[i] + i for i in cols)) == len(
                    set(vec[i] - i for i in cols))):
                res.append(vec)
        return res

    @exeTime
    def queen8_rec(self):
        '''使用回溯法解决八皇后问题

        如果冲突，则返回上一层，将该层的皇后右移一格，再继续判断
        '''
        board = list(range(8))
        row = 0
        self.doQueen(board, row, res)
        return res

    def doQueen(self, board, row, res):
        if row == 8:  #到达第九行，说明前面八行没有冲突，是一个成功的摆放
            res.append(board)
            return True
        for i in range(len(board)):
            if self.check(board, i, board[i]):  #当前位置不冲突
                board[row] = i
                if self.doQueen(board, row + 1, res):
                    return True  #如果需要找到所有的解，则删掉if
        return False

    def check(self, board, row, col):
        for i in range(row):
            if abs(row - i) == abs(col - board[i]):
                return False
        return True


if __name__ == "__main__":
    so = Solution()
    print('=' * 5, '解法1:全排列', '=' * 5)
    res = so.queen8()
    print(len(res))
    print('=' * 5, '解法2:回溯法', '=' * 5)
    res1 = so.queen8_rec()
    print(len(res1))
