from exeTime import exeTime


class Solution:
    @exeTime
    def getMaxValue(self, grid):
        if not grid: return 0
        valueOfEach = grid[:][:]
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row > 0 and col > 0:
                    valueOfEach[row][col] = max(
                        valueOfEach[row - 1][col],
                        valueOfEach[row][col - 1]) + grid[row][col]
                elif row > 0:
                    valueOfEach[row][col] = valueOfEach[
                        row - 1][col] + grid[row][col]
                elif col > 0:
                    valueOfEach[row][col] = valueOfEach[row][
                        col - 1] + grid[row][col]
        return valueOfEach[row][col]

    @exeTime
    def getMaxValue2(self, grid):
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        valueOfEach = [0 for i in range(cols)]
        for row in range(rows):
            for col in range(cols):
                left, up = 0, 0
                if row > 0:
                    up = valueOfEach[col]
                if col > 0:
                    left = valueOfEach[col - 1]
                valueOfEach[col] = max(left, up) + grid[row][col]
        return valueOfEach[col]


if __name__ == "__main__":
    so = Solution()
    grid = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(so.getMaxValue(grid))
    grid = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(so.getMaxValue2(grid))
