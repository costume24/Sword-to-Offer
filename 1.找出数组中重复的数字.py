# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
from exeTime import exeTime


@exeTime
def duplicate(numbers, duplication):
    # write code here
    if not numbers:
        return False
    for item in numbers:
        if item < 0 or item > len(numbers) - 1:
            return False
    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                duplication[0] = numbers[i]
                return True
            else:
                tmp = numbers[i]
                numbers[i] = numbers[tmp]
                numbers[tmp] = tmp
    return False


@exeTime
def duplicate2(numbers, duplication):
    dic = {}
    if not numbers:
        return False
    for item in numbers:
        if item < 0 or item > len(numbers) - 1:
            return False
        elif item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    for key in dic:
        if dic[key] > 1:
            duplication[0] = key
            return True
    return False


if __name__ == "__main__":
    numbers = []
    duplication = [-1]
    duplicate2(numbers, duplication)

