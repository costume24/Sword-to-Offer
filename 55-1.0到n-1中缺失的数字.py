from exeTime import exeTime


def get_missing_number(n):
    '''一个长度为n的递增排序数组，所有数字唯一且在0到n-1之间
    有且仅有一个数字不在数组中，找出该数字
    直观解法：
        求出0到n-1的和，然后求出当前数组的和，两者相减即可
        时间复杂度为O(n)，没有利用到数组为递增这一特性
    
    二分解法：
        根据题目特性，在缺失数字之前，所有数字的值和下标相等
        在缺失数字之后，所有数字的值不等于下标，可用二分查找
        找到第一个不相等的数字
    '''
    left = 0
    right = len(n) - 1
    while left <= right:
        mid = int((right + left) >> 1)
        if mid == n[mid]:
            left = mid + 1
        elif mid < n[mid]:
            # 两种情况表明已经找到：
            # （1）左边的数字等于下标
            # （2）已到达数组开头（说明缺失了第一个数字0）
            if (mid > 0 and n[mid - 1] == mid - 1) or mid == 0:
                return mid
            else:
                right = mid - 1
    if left == len(n):
        return len(n)
    return -1


if __name__ == "__main__":
    miss = 0
    end = 10
    n = list(range(miss))
    n.extend(list(range(miss + 1, end)))
    print(get_missing_number(n))