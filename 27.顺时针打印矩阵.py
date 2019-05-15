from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    @exeTime
    def printMatrix(self, matrix):
        if not matrix: return None
        n, m = len(matrix), len(matrix[0])
        number = n * m
        k, i, j, flag = 0, 0, 0, 'right'
        res = []
        while k <= number - 1:

            res.append(matrix[i][j])
            matrix[i][j] = None
            k += 1
            if flag == 'right':
                if j + 1 < m and matrix[i][j + 1] != None: j += 1
                else:
                    i += 1
                    flag = 'down'
            elif flag == 'down':
                if i + 1 < n and matrix[i + 1][j] != None: i += 1
                else:
                    j -= 1
                    flag = 'left'
            elif flag == 'left':
                if j - 1 >= 0 and matrix[i][j - 1] != None: j -= 1
                else:
                    i -= 1
                    flag = 'up'
            elif flag == 'up':
                if i - 1 >= 0 and matrix[i - 1][j] != None: i -= 1
                else:
                    j += 1
                    flag = 'right'
        return res

    @exeTime
    def printMatrix2(self, matrix):
        '''用左上和右下来定位一圈需要打印的数据
        打印一圈后，左上前进一步，右下后退一步
        '''
        if not matrix: return None
        n, m = len(matrix), len(matrix[0])
        left, top, right, bottom = 0, 0, m - 1, n - 1
        res = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return res


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    so = Solution()
    print(so.printMatrix(matrix))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(so.printMatrix2(matrix))
