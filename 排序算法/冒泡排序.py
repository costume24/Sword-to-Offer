from multitimes import multitimes


@multitimes
def bubble_sort(array):
    '''冒泡排序

    每一趟都将相邻的两个数字比较，把较大的数字移到右边

    复杂度分析：
        1. 最好情况：已经有序，时间复杂度为O(n)
        2. 最坏情况：数组逆序，时间复杂度为O(n^2)
        3. 平均情况：O(n^2)
    
    是否稳定：
        是
    '''
    if not array:
        return
    alen = len(array)
    for i in range(alen):
        flag = False
        for j in range(alen - 1 - i):  # 每一趟排序后，最大的i+1个元素已经有序
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:  # 如果没有交换，即已经有序，结束算法
            break
    return array


if __name__ == "__main__":
    array = [6, 5, 3, 2, 4, 1, 8, 7]
    #array = [0, 5, 3, 2, 2]
    print(bubble_sort(array))
