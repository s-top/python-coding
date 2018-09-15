# # import sys
# # class Solution:
# #     def ReverseNum(self, myList):
# #         result = []
# #         return result
# #
# # if __name__ == '__main__':
# #     number = int(input())
# #     print(number)
# #     t = int(sys.stdin.readline().strip())
# #     print(t)
# #     resList = []
# #     for i in range(t):
# #         n = int(sys.stdin.readline())
# #         array = list(map(int, sys.stdin.readline().strip().split()))
# #
# #     n = int(input())
# #     numsA = sys.stdin.readline().strip().split()
# #     numsB = sys.stdin.readline().strip().split()
#
# # def getAllStr(string):
# #     result = []
# #     index = 0
# #     while index < len(string):
# #         for i in range(index + 1, len(string) + 1):
# #             result.append(string[index:i])
# #         index = index + 1
# #     return result
# # ========================================================
# # def func(s):
# #     if len(s) <1:
# #         return s
# #     return func(s[1:])+s[0]
#
# # import sys
# #
# # if __name__ == '__main__':
# #     # 1->2->3->4->5
# #     strA = sys.stdin.readline().strip().split("=")
# #     a = strA.split("->")
# #     n = int(strA[1])
# #     for i in range(len(res)):
#     # result = str.encode(strA)
#     # index = []
#     # string = []
#     # for i in range(len(result)):
#     #     if result[i] >= 49 and result[i] <= 57:
#     #         index.append(i)
#     #     else:
#     #         string.append(i)
#     # print(index)
#     # print(string)
#     # dataIndex = []
#     # dataString = []
#     # j = 1
#     # for i in range(j,len(index)):
#     #     if index[i - 1] + 1 != index[i]:
#     #         dataIndex.append(index[i-1])
#     # for i in range(j, len(string)):
#     #     if string[i - 1] + 1 != string[i]:
#     #         dataString.append(string[i-1])
#     #             # res = res + strA[index[i - 1]:index[i]]
#     #     # data.append(res)
#     # print(dataIndex)
#     # print(dataString)
#     # resultIndex = []
# # ======================================================
# # import sys
# # # 用来判断坐标是否合法
# # def check_valid(mg, x, y):
# #     if x >= 0 and x < len(mg) and y >= 0 and y < len(mg[0]) \
# #             and mg[x][y] == 1:
# #         return True
# #     else:
# #         return False
# #
# #
# # # 迷宫结果优化
# # def process(step):
# #     # 先识别哪些无路可走的点的下一个点
# #     change_records = []
# #     for i in range(len(step) - 1):
# #         if (abs(step[i][0] - step[i + 1][0]) == 0 and abs(step[i][1] - step[i + 1][1]) == 1) or \
# #                 (abs(step[i][0] - step[i + 1][0]) == 1 and abs(step[i][1] - step[i + 1][1]) == 0):
# #             pass
# #         else:
# #             change_records.append(i + 1)
# #     print(change_records)
# #
# #     # 然后根据这些点识别出这个点的最远回退点
# #     clip_nums = []
# #     for i in change_records:
# #         for j in range(i):
# #             if (abs(step[j][0] - step[i][0]) == 0 and abs(step[j][1] - step[i][1]) == 1) or \
# #                     (abs(step[j][0] - step[i][0]) == 1 and abs(step[j][1] - step[i][1]) == 0):
# #                 break
# #             clip_nums.append((j, i))
# #     print(clip_nums)
# #
# #     # 注意回退点之间的包含关系, 逆序处理, 是为了规避顺序对列表进行处理后下标偏移的问题
# #     record = []
# #     for i in clip_nums[::-1]:
# #         if not (i[0] in record or i[1] in record):
# #             step = step[:i[0] + 1] + step[i[1]:]
# #         record += list(range(i[0], i[1]))
# #     print(step)
# #
# #
# # step = []
# # n = 6
# #
# # def walk(mg, x, y):
# #     global step
# #     if x == 5 and y == 5:
# #         step.append((x, y))
# #         process(step)
# #         print("Walk success!")
# #         sys.exit()
# #
# #     if check_valid(mg, x, y):
# #         step.append((x, y))
# #         mg[x][y] = 2
# #         walk(mg, x, y + 1)
# #         walk(mg, x + 1, y)
# #
# #
# # mg = [[1, 0, 0, 1, 1, 0],
# #       [1, 1, 0, 0, 0, 1],
# #       [0, 0, 0, 1, 0, 1],
# #       [0, 1, 1, 1, 0, 1],
# #       [0, 1, 0, 1, 0, 1],
# #       [1, 1, 1, 0, 0, 0]]
# #
# # walk(mg, 0, 0)  # 从5, 0这个点开始走迷宫, 出口为0, 0
# # =================================================
# #
# # import sys
# # if __name__ == '__main__':
# #     number = int(input())
# #     for i in range(number):
# #         n = int(input())
# #         x = []
# #         y = []
# #         resX = []
# #         resY = []
# #         for i in range(n):
# #             data = sys.stdin.readline().strip().split()
# #             x.append(int(data[0]))
# #             y.append(int(data[1]))
# #             resX.append(int(data[0]))
# #             resY.append(int(data[1]))
# #         for i in range(len(x)):
# #             for j in range(len(y)):
# #                 if x[i] == y[j] and i != j:
# #                     resX.remove(x[i])
# #                     resY.remove(y[j])
# #                     break
# #         if len(resX) <= 1 and len(resY) <= 1:
# #             print("yes")
# #         else:
# #             print("no")
# # =======================================================
# # import sys
# #
# # def getNum(data, index, a):
# #     if data[index - 1] > data[index]:
# #         k = data.index(data[index])
# #         data.pop(k)
# #         a = a + 1
# #     if data[index] > data[index + 1]:
# #         k = data.index(data[index])
# #         data.pop(k)
# #         a = a + 1
# #     return a
# #
# # if __name__ == '__main__':
# #     num = int(sys.stdin.readline().strip())
# #     content = sys.stdin.readline().strip().split()
# #     data = []
# #     for i in range(len(content)):
# #         data.append(int(content[i]))
# #     s = 0
# #     for i in range(1, len(content) - 1):
# #         s = s + getNum(data, i, 0)
# #
# #     print(s)
#
# import sys
#
# # 7 2
# # 1 2 3 -2 3 -10 3
#
# def getMax(num_list):
#     length = len(num_list)
#     max_value = -10000000000
#     tmp = 0
#     p = 0
#     q = 0
#     t = []
#     for i in range(length):
#         if tmp + num_list[i] < num_list[i]:
#             p = i
#             q = 1
#         else:
#             q += 1
#         tmp = max(tmp + num_list[i], num_list[i])
#         max_value = max(max_value, tmp)
#         if tmp == max_value:
#             t.append((p, (p + q)))
#     return max_value, t[-1]
# if __name__ == '__main__':
#     num = sys.stdin.readline().strip().split()
#     a = int(num[0])
#     b = int(num[1])
#     content = sys.stdin.readline().strip().split()
#     data = []
#     for i in range(len(content)):
#         data.append(int(content[i]))
#     indexList = []
#     for j in range(len(data)):
#         if data[j] < 0:
#             indexList.append(j)
#     result1 = 0
#     a = []
#     for k in range(len(indexList)):
#         b = 0
#         for j in range(0,indexList[k]):
#             b = b + data[j]
#         a.append(b)
#         # for j in range(0, indexList[k]):
#
#
#     result = 0
#
#     for i in range(b):
#         dataMax, index = getMax(data)
#         result = result + dataMax
#         if index[1] < len(data):
#             data = data[index[1]:]
#
# import math
# import sys
# #定义点的函数
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x=x
#         self.y=y
#     def getx(self):
#         return self.x
#     def gety(self):
#         return self.y
#     def setx(self, value):
#         self.x = value
#     def sety(self, value):
#         self.y = value
# #定义直线函数
# class Getlen:
#     def __init__(self,p1,p2):
#         self.x = p1.getx()-p2.getx()
#         self.y = p1.gety()-p2.gety()
#         #用math.sqrt（）求平方根
#         self.len = math.sqrt((self.x**2)+(self.y**2))
#     #定义得到直线长度的函数
#     def getlen(self):
#         return self.len
#
# # 2 -1 0 5 3
# # 0 2
# # 5 2
#
# if __name__ == '__main__':
#     num = sys.stdin.readline().strip().split()
#     n = int(num[0])
#     p1 = Point(int(num[1]), int(num[2]))
#     p2 = Point(int(num[3]), int(num[4]))
#     data = []
#     resultList1 = []
#     resultList2 = []
#     r1 = 0
#     r2 = 0
#     for i in range(n):
#         content = sys.stdin.readline().strip().split()
#         # data.append((int(content[0]),int(content[1])))
#         p = Point(int(content[0]),int(content[1]))
#         if Getlen(p, p1).len <= Getlen(p, p2).len:
#             resultList1.append(Getlen(p, p1).len)
#         else:
#             resultList2.append(Getlen(p, p2).len)
#
#     r1 = max(resultList1)
#     r2 = max(resultList2)
#     print(int((r1**2)+(r2**2)))

# def sort_(l):
#     if len(l) <= 1:
#         return l
#     mid = l[0]
#     low = [item for item in l if item < mid]
#     high = [item for item in l if item > mid]
#     return sort_(low) + [mid] + sort_(high)
# import sys
# if __name__ == '__main__':
#     # 10, 1, 3, 5, 5, 8
#     num = sys.stdin.readline().strip().split(", ")
#     numList = []
#     for i in range(len(num)):
#         numList.append(int(num[i]))
#     result = sort_(numList)
#     res = str(result[0])
#     for i in range(1, len(result)):
#         res = res + "," + str(result[i])
#     print(res)

# 快速排序思想
def getRes_QuickSort(nums, target):
    nums = sorted(nums)
    len1 = len(nums)
    res = []
    if len1 >= 2:
        low, high = 0, len1 - 1
        while low < high:
            if nums[low] + nums[high] == target:
                res.append((nums[low], nums[high]))
                low += 1
                high -= 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        return res

import sys
if __name__ == "__main__":
    data = sys.stdin.readline().strip().split("|")
    nums = data[0].split(",")
    dataNums = []
    for i in range(len(nums)):
        dataNums.append(int(nums[i]))
    target = int(data[1])
    result = (getRes_QuickSort(dataNums, target))
    n = 0
    print(dataNums)
    for i in range(len(dataNums)):
        if 2 * dataNums[i] == target:
            print(dataNums[i])
            n = n + 1
            print(n)
    print(result)
    if result == []:
        print(n)
    else:
        a = 0
        for i in result:
            a = a + 1
        print(a + n)
