from exeTime import exeTime


class Solution:
    @exeTime
    def reOrderArray(self, array):
        # write code here
        single = []
        double = []
        for item in array:
            if item % 2 == 0: double.append(item)
            else: single.append(item)
        return single + double


if __name__ == "__main__":
    so = Solution()
    array = [1, 5, 8, 7, 4, 3, 10, 52, 98, 5, 3, 6]
    print(so.reOrderArray(array))
