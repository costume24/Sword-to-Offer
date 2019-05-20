from exeTime import exeTime


@exeTime
def mergeSort(lyst):
    buffer = [0] * len(lyst)
    mergeSortHelper(lyst, buffer, 0, len(lyst) - 1)


def mergeSortHelper(lyst, buffer, start, end):
    if start < end:
        mid = int((start + end) / 2)
        mergeSortHelper(lyst, buffer, start, mid)
        mergeSortHelper(lyst, buffer, mid + 1, end)
        merge(lyst, buffer, start, mid, end)
    return lyst


def merge(lyst, buffer, start, mid, end):
    '''合并过程
    两个子数组分别为lyst[start:mid]和lyst[mid+1:end]
    使用两个指针，分别指向两个子数组，依次选择较小的元素放入新数组
    '''
    p1 = start
    p2 = mid + 1
    for i in range(start, end + 1):
        if p1 > mid:
            buffer[i] = lyst[p2]
            p2 += 1
        elif p2 > end:
            buffer[i] = lyst[p1]
            p1 += 1
        elif lyst[p1] <= lyst[p2]:
            buffer[i] = lyst[p1]
            p1 += 1
        else:
            buffer[i] = lyst[p2]
            p2 += 1
    for i in range(start, end + 1):
        lyst[i] = buffer[i]
    return lyst


if __name__ == "__main__":
    lyst = [3, 7, 6, 5, 4, 8, 2, 1]
    mergeSort(lyst)
    print(lyst)
