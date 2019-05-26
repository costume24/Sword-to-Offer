from multitimes import multitimes


def bio_search_sort(array):
    '''二分查找排序

    也是直接插入排序的一个修改版本，改进之处在于采用二分法查找新元素的插入位置

    步骤：
        1. 从第一个元素开始，默认第一个元素有序
        2. 取出下一个元素，用二分法查找其应该插入的位置
        3. 重复1,2直到结束
    '''
    if not array:
        return
