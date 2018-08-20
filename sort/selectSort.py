# 选择排序的思想：
# 第一趟，从n个记录中找出关键码最小的记录与第一个记录交换；
# 第二趟，从第二个记录开始的n-1 个记录中再选出关键码最小的记录与第二个记录交换；
# 以此类推.....
# 第i 趟，则从第i 个记录开始的n-i+1 个记录中选出关键码最小的记录与第i 个记录交换，
# 直到整个序列按关键码有序。

def selectSort(lists):
    count = len(lists)
    for i in range(count):
        temp = min(lists[i:])
        index = lists.index(temp)
        lists[index] = lists[i]
        lists[i] = temp
    return lists

# bug 倘若出现重复的情况则失效
lists = [49,38,65,97,76,13,27]
print(selectSort(lists))