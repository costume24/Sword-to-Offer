from multitimes import multitimes


def radix_sort(array):
    '''基数排序

    线性时间排序，不同比较。其思想是按照每一位上的数字排序。

    步骤：
        1. 从最低位开始，按照该位上的数字将元素放入相应的桶中
        2. 按照桶的顺序，把桶中数字取出，放回原数组，则此时原数组中的数已经按照当前比较数位排好序
        3. 比较数位向左移动一为，重复1,2，直到到达最大数 
    '''
    if not array:
        return
    placement = 1  # 用于依次提取每一位上的数字，取值为1,10,100，...
    max_digit = max(array)
    while placement < max_digit:
        buckets = [list() for _ in range(10)]  # 为当前位的每个数字创建一个桶
        for num in array:
            tmp = int((num / placement) % 10)
            buckets[tmp].append(num)  # 把每个元素按照当前位的数字放到对应的桶中
        a = 0
        for b in range(10):
            buck = buckets[b]  # 按照桶的顺序
            for num in buck:
                array[a] = num  # 把桶中数字依次放入原数组中
                a += 1
        placement *= 10
    return array


if __name__ == "__main__":
    array = [27, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25]
    print(radix_sort(array))