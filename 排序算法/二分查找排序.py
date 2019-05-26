from multitimes import multitimes


def bin_search_sort(array):
    '''二分查找排序

    也是直接插入排序的一个修改版本，改进之处在于采用二分法查找新元素的插入位置

    步骤：
        1. 从第一个元素开始，默认第一个元素有序
        2. 取出下一个元素，用二分法查找其应该插入的位置
        3. 重复1,2直到结束
    '''
    if not array:
        return
    alen = len(array)
    for i in range(alen):
        tmp = array[i]
        index = 0
        index = bin_search(array, 0, i, index, tmp)
        for k in range(i-1, index-1,-1):
            array[k + 1] = array[k]
        array[index]=tmp
    return array


def bin_search(array, start, end, res, aim):
    if start < end:
        mid = int((start + end) / 2)
        if array[mid] == aim:
            return mid
        elif array[mid] > aim:
            res = bin_search(array, start, mid - 1, res, aim)
        else:
            res = bin_search(array, mid + 1, end, res, aim)
    elif start >= end:
        if array[start] == aim:
            return start
        elif array[start] > aim:
            return start
        else:
            return start + 1
    return res


if __name__ == "__main__":
    array = [1, 3, 5, 6, 7, 9, 12, 15]
    array = [6, 5, 3, 2, 4, 1, 8, 7]
    index = 0
    #print(bin_search(array, 0, len(array), index, 4))
    print(bin_search_sort(array))
