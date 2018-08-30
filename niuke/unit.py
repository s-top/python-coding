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

def getAllStr(string):
    result = []
    index = 0
    while index < len(string):
        for i in range(index + 1, len(string) + 1):
            result.append(string[index:i])
        index = index + 1
    return result

import sys

if __name__ == '__main__':
    strA = sys.stdin.readline().strip()
    strB = sys.stdin.readline().strip()
    a = getAllStr(strA)
    b = getAllStr(strB)
    result = []
    for i in range(len(b)):
        if b[i] in a:
            result.append(len(b[i]))
    if result:
        print(max(result))
    else:
        print(0)