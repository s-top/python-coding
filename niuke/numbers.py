
# # 数字拆分
# def SpliteUnit(lens, step, arr, index, results):
#     if lens == 0:
#         print(arr[:index])
#         results.append(arr[:index])
#     for i in range(step, lens + 1, 1):
#         arr[index] = i
#         SpliteUnit(lens - i, i, arr, index + 1, results)
#
# num = 15
# result = []
# tmp_arr = [0] * num
# SpliteUnit(num, 1, tmp_arr, 0, result)
# ====================================================
# # 12345 拆分 被3整除
# if __name__ == '__main__':
#     number = int(input())
#     numberStr = str(number)
#     result = []
#     i = 0
#     while i < len(numberStr):
#         for j in range(1, len(numberStr) + 1):
#             if i < j:
#                 if int(numberStr[i:j]) % 3 == 0:
#                     result.append(numberStr[i:j])
#                     i = j
#                     break
#     print(len(result))
# =====================================================
# [0,1,2,3,4,5,6,7,8,9] -> 0 1 1 1 1 1 1 1 1 0
# import sys
# if __name__ == '__main__':
#     t = sys.stdin.readline().strip().split()
#     result = []
#     for i in range(len(t)):
#         if t[i] == "0":
#             result.append(str(i))
#     strList = []
#     strList.append("0123456789")
#     data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for i in range(len(result)):
#         data.remove(result[i])
#     strList.append("".join(data))
#     for i in range(len(result)):
#         dataA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         dataA.remove(result[i])
#         strList.append("".join(dataA))
#     # print(sorted(strList))
#     for i in range(len(strList)):
#         print(strList[i])
# ========================================================================
# 复数运算
# class Complex:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def multi(self):
#         return Number(self.x.r * self.y.r - self.x.im * self.y.im, self.y.r * self.x.im + self.x.r * self.y.im).show()
# class Number:
#     def __init__(self, x, y):
#         self.r = x
#         self.im = y
#     def show(self):
#         return self.r, self.im
#
# def getResult(numberA1,numberB1,numberA2,numberB2):
#     c1 = Number(numberA1,numberB1)
#     c2 = Number(numberA2,numberB2)
#     c = Complex(c1, c2)
#     return c.multi()
#
# if __name__ == '__main__':
#     dataA = []
#     dataB = []
#     a = []
#     b = []
#     for i in range(10):
#         dataA.append(int(input()))
#     for i in range(10):
#         dataB.append(int(input()))
#     for i in range(0, 10, 2):
#         a.append(str(dataA[i]) + "," + str(dataA[i+1]))
#         b.append(str(dataB[i]) + "," + str(dataB[i+1]))
#     a.reverse()
#     b.reverse()
#     result = []
#     for k in range(8, -1, -1):
#         n = 0
#         num = 0
#         for i in range(5):
#             for j in range(5):
#                 if i + j == k:
#                     r, im = getResult(int(a[i].split(",")[0]), int(a[i].split(",")[1]), int(b[j].split(",")[0]), int(b[j].split(",")[1]))
#                     n = n + r
#                     num = num + im
#         result.append(n)
#         result.append(num)
#     for i in range(len(result)):
#         print(result[i])
# ==========================================
# 股票价格
# import sys
# if __name__ == '__main__':
#     t = sys.stdin.readline().strip().split()
#     num = []
#     result = []
#     for i in range(len(t)):
#         number = 0
#         for j in range(i + 1):
#             number = number + int(t[j])
#         num.append(number)
#         sum = int(t[i]) * (i + 1)
#         result.append(sum)
#     print(num)
#     print(result)
# =====================================================

# !usr/bin/env python
# encoding:utf-8

# import re
# import sys
# def judge_legal_ip(one_str):
#     compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
#     if compile_ip.match(one_str):
#         return True
#     else:
#         return False
# def judge_legal_ip2(one_str):
#     if '.' not in one_str:
#         return False
#     elif one_str.count('.') != 3:
#         return False
#     else:
#         flag = True
#         one_list = one_str.split('.')
#         for one in one_list:
#             try:
#                 one_num = int(one)
#                 if one_num >= 0 and one_num <= 255:
#                     pass
#                 else:
#                     flag = False
#             except:
#                 flag = False
#         return flag
#
# ip_str = sys.stdin.readline().strip()
# print(judge_legal_ip(ip_str))
import sys
data = sys.stdin.readline().strip().split("=")
print(data)
n = data[1]
array = []
for i in range(n):
    if i == 0:
        array.append(0)
    else:
        array.append(2 * i - 1)
sum = 0
for i in range(len(array)):
    flag = 0
    for j in range(2, array[i]):
        if array[i] % j == 0:
            flag = 1
            break
    if flag == 0:
        sum = sum + array[i]
print(sum)