# 二分查找的思想：
# (1)确定中间位置K
# (2)将查找的值T与array[k]比较。若相等，查找成功返回此位置；否则确定新的查找区域，继续二分查找。

import math

def binarySearch(array, t):
    array = sorted(array)
    low, height = 0, len(array) - 1
    while low < height:
        mid = int((low + height) / 2)
        # print(array[mid])
        if array[mid] < t:
            low = mid + 1
        elif array[mid] > t:
            height = mid - 1
        else:
            return array[mid]
    return -1

# list为偶数正常，为奇数时有bug

array = [1, 2, 3, 34, 56, 57, 78, 87]

print(binarySearch(array, 57))






