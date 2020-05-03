"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""


def duplicate(numbers, duplication):
    if not numbers:
        return
    if len(numbers) == 1:
        return
    for i in range(len(numbers)):
        pop_num = numbers.pop(0)
        if pop_num in numbers:
            return pop_num


if __name__ == '__main__':
    print(duplicate([2, 3, 1, 0, 2, 5, 3], duplication=None))
