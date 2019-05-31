from exeTime import exeTime


def shell_sort(array):
    '''希尔排序

    属于插入排序的一种，是对直接插入排序的改进版本。
    第一趟排序过后，数组基本有序，到最后一步时，就是直接插入排序。
    但此时数组已基本有序，时间复杂度为O(n)。
    
    步骤：
        1. 按照增量将数组分组，一半初始化增量为数组长度的一半，组数等于增量的值
        2. 每组内部进行直接插入排序
        3. 将增量减少一半，重复1,2，直到增量为1

    复杂度分析：
        1. 最好情况：数组已经有序，只需要O(n)
        2. 最坏情况：数据逆序，根据采取的序列不同而不同，初始化为长度的一半的话，仍为O(n^2)
            采取其他增量序列，可以达到O(n(log n)^2)

    是否稳定：
        否。虽然单次的插入排序是稳定的，但是两个相等元素可能分在不同的组，在不同的
        插入排序中，其次序有可能发生变化
    '''
    if not array:
        return
    alen = len(array)
    gap = int(alen / 2)
    while gap > 0:
        for i in range(gap, alen):
            tmp = array[i]
            j = i
            while j >= gap and array[j - gap] > tmp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = tmp
        gap = int(gap / 2)
    return array


if __name__ == "__main__":
    array = [6, 5, 3, 2, 4, 1, 8, 7]
    print(shell_sort(array))