# 冒泡排序思想：
# 一次比较两个元素，如果它们的顺序错误就把它们交换过来

# 一趟冒泡排序的算法是：
# 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
# 针对所有的元素重复以上的步骤，除了最后一个；
# 重复步骤1~3，直到排序完成

def bubbleSort(myList):
    length = len(myList)
    for i in range(length):
        # for j in range(length - i - 1):
        #     # 从小到大是>
        #     # 从大到小是<
        #     if myList[j] > myList[j + 1]:
        #         temp = myList[j + 1]
        #         myList[j + 1] = myList[j]
        #         myList[j] = temp

        for j in range(i + 1, length):
            if myList[i] > myList[j]:
                myList[i], myList[j] = myList[j], myList[i]

    return myList

myList = [49,38,65,97,76,13,27,49]
print(myList)
print("Bubble Sort: ")
print(bubbleSort(myList))