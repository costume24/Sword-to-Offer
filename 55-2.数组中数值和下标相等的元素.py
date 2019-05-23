from exeTime import exeTime


def get_num_same_as_index(n):
    '''
    由于数组单调递增且数字唯一，因此可用二分查找
    '''
    if not n: return
    left = 0
    right = len(n)
    while left <= right:
        mid = int((right + left) / 2)
        if n[mid] == mid: return mid
        elif n[mid] > mid:
            right = mid - 1
        elif n[mid] < mid:
            left = mid + 1
    return


if __name__ == "__main__":
    n = [0, 2, 4, 5, 6]
    print(get_num_same_as_index(n))
