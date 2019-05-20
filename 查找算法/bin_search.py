from exeTime import exeTime


def dobin(data, k, start, end):
    '''递归写法，效率较低
    '''
    if not data or start > end: return -1
    mid = int((end + start) / 2)
    if data[mid] > k:
        return dobin(data, k, start, mid - 1)
    elif data[mid] < k:
        return dobin(data, k, mid + 1, end)
    else:
        return mid
    return -1


@exeTime
def binsearch(data, k):
    return dobin(data, k, 0, len(data) - 1)


@exeTime
def binsearch2(data, k):
    '''循环解法，效率较高
    '''
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if data[mid] == k:
            return mid
        elif data[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    data = list(range(9999))
    k = 0
    print(binsearch(data, k))
    print(binsearch2(data, k))
