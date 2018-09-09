# import sys
# class Solution:
#     def ReverseNum(self, myList):
#         result = []
#         return result
#
# if __name__ == '__main__':
#     number = int(input())
#     print(number)
#     t = int(sys.stdin.readline().strip())
#     print(t)
#     resList = []
#     for i in range(t):
#         n = int(sys.stdin.readline())
#         array = list(map(int, sys.stdin.readline().strip().split()))
#
#     n = int(input())
#     numsA = sys.stdin.readline().strip().split()
#     numsB = sys.stdin.readline().strip().split()

# def getAllStr(string):
#     result = []
#     index = 0
#     while index < len(string):
#         for i in range(index + 1, len(string) + 1):
#             result.append(string[index:i])
#         index = index + 1
#     return result

import sys

def getNum(data, index, a):
    if data[index - 1] > data[index]:
        k = data.index(data[index])
        data.pop(k)
        a = a + 1
    if data[index] > data[index + 1]:
        k = data.index(data[index])
        data.pop(k)
        a = a + 1
    return a

if __name__ == '__main__':
    num = int(sys.stdin.readline().strip())
    content = sys.stdin.readline().strip().split()
    data = []
    for i in range(len(content)):
        data.append(int(content[i]))
    s = 0
    for i in range(1, len(content) - 1):
        s = s + getNum(data, i, 0)

    print(s)
