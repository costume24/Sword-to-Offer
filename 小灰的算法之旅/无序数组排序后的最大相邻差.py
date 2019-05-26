from exeTime import exeTime
from multitimes import multitimes
import numpy as np


@multitimes
def get_max_sorted_dist1(array):
    '''用计数排序的思想

    1. 找到最大值和最小值的下标，得到k=max-min+1和偏移量d=min
    2. 新建一个长度为k的数组a，初始化为0
    3. 遍历原数组，若原数组元素为i，则a[i-d]的值加1
    4. 遍历新数组，找到最长连续0的长度，再加1即可

    缺点：
        若数组元素相差悬殊，如数组为[1,100,10000]
        则需要创建长度为10000的数组，效率极低
    '''
    if not array: return
    min_x = min(array)
    max_x = max(array)
    min_id = array.index(min_x)
    max_id = array.index(max_x)
    k = max_x - min_x + 1
    a = [0 for i in range(k)]
    for item in array:
        a[item - min_x] += 1
    cnt = 0
    max_cnt = 0
    for i in range(k):
        if a[i] == 0:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0
    return max_cnt + 1


@multitimes
def get_max_sorted_dist2(array):
    '''用桶排序的思想

    1. 原始数组长度为n，则创建n个桶，每个桶的区间为(max-min)/(n-1)
    2. 遍历原始数组，将数放入每个桶中，并记录每个桶的最大最小值
    3. 遍历桶，计算每个桶的最大值与其右边的桶的最小值的差
    4. 差的最大值即为所求
    '''
    if not array: return
    alen = len(array)
    min_x = min(array)
    max_x = max(array)
    interval = (max_x - min_x) / (alen - 1)
    res = {}
    min_max_for_each = {}
    for i in range(alen):
        res[i] = []
        min_max_for_each[i] = [np.inf, -np.inf]
    for i in range(alen):
        item = array[i]
        id = int((item - min_x) / interval)
        res[id].append(item)
        if item < min_max_for_each[id][0]:
            min_max_for_each[id][0] = item
        if item >= min_max_for_each[id][1]:
            min_max_for_each[id][1] = item
    max_diff = -np.inf
    i = -1
    while i < alen:
        i += 1
        max_now = min_max_for_each[i][1]
        while min_max_for_each[i + 1][0] is np.inf:
            i += 1
        diff = min_max_for_each[i + 1][0] - max_now
        if diff > max_diff:
            max_diff = diff
    return max_diff


@multitimes
def get_max_sorted_dist3(array):
    if not array: return
    max_diff = -np.inf
    array = sorted(array)
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if diff > max_diff:
            max_diff = diff
    return max_diff


if __name__ == "__main__":
    array = [2, 6, 3, 4, 5, 10, 9]
    print(get_max_sorted_dist1(array))
    print(get_max_sorted_dist2(array))
    print(get_max_sorted_dist3(array))
