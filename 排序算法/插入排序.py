from exeTime import exeTime


def insertion_sort(array):
    '''直接插入排序
    类似于打扑克牌时的场景，每次将一个数与其他数字比较，插入到相应的位置上

    步骤：
        1. 从第一个元素开始，默认第一个元素已排序
        2. 取出下一个元素，在已排序的数组中从后往前扫描
        3. 找到第一个小于等于该元素的位置
        4. 将其插入到该位置后面

    复杂度分析：
        1. 最好情况：数组已经有序，每插入一个元素，只需要考虑前一个元素，时间复杂度为O(n)
        2. 最坏情况：数组逆序，每插入一个元素，需要考虑前面所有元素，时间复杂度为O(n^2)
        3. 平均情况：时间复杂度为O(n^2)

    是否是稳定排序：
        是
    '''
    if not array:
        return
    for i in range(len(array)):
        tmp = array[i]
        j = i - 1
        while j >= 0 and array[j] > tmp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp

    return array


if __name__ == "__main__":
    array = [6, 5, 3, 2, 4, 1, 8, 7]
    print(insertion_sort(array))
