# 快速排序思想：
# 首先任意选取一个数据（通常选用数组的第一个数）作为关键数据
# 然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面
# 这个过程称为一趟快速排序

# 一趟快速排序的算法是：
# 1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
# 2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
# 3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
# 4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
# 5）重复第3、4步，直到i=j；
# (3,4步中，没找到符合条件的值，即3中A[j]不小于key,
# 4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。
# 找到符合条件的值，进行交换的时候i， j指针位置不变。
# 另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）

def QuickSort(myList, start,end):
    # 判断start是否小于end,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]
        while i < j:
            while i < j and myList[j] >= base:
                j = j - 1
            # print("j:" + str(j))
            myList[i] = myList[j]

            while i < j and myList[i] <= base:
                i = i + 1
            # print("i:" + str(i))
            myList[j] = myList[i]
            # print("myList:", myList)
        myList[i] = base
        # 递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)

myList = [49,38,65,97,76,13,27,49]
print("Quick Sort: ")
QuickSort(myList,0,len(myList)-1)
print(myList)
# ==================================================
# 49,38,65,97,76,13,27,49
# Quick Sort:
# j:6
# i:2
# myList: [27, 38, 65, 97, 76, 13, 65, 49]
# j:5
# i:3
# myList: [27, 38, 13, 97, 76, 97, 65, 49]
# j:3
# i:3
# myList: [27, 38, 13, 97, 76, 97, 65, 49]
# j:2
# i:1
# myList: [13, 38, 38, 49, 76, 97, 65, 49]
# j:1
# i:1
# myList: [13, 38, 38, 49, 76, 97, 65, 49]
# j:7
# i:5
# myList: [13, 27, 38, 49, 49, 97, 65, 97]
# j:6
# i:6
# myList: [13, 27, 38, 49, 49, 65, 65, 97]
# j:4
# i:4
# myList: [13, 27, 38, 49, 49, 65, 76, 97]