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
# ========================================================
# def func(s):
#     if len(s) <1:
#         return s
#     return func(s[1:])+s[0]

# import sys
#
# if __name__ == '__main__':
#     # 1->2->3->4->5
#     strA = sys.stdin.readline().strip().split("=")
#     a = strA.split("->")
#     n = int(strA[1])
#     for i in range(len(res)):
    # result = str.encode(strA)
    # index = []
    # string = []
    # for i in range(len(result)):
    #     if result[i] >= 49 and result[i] <= 57:
    #         index.append(i)
    #     else:
    #         string.append(i)
    # print(index)
    # print(string)
    # dataIndex = []
    # dataString = []
    # j = 1
    # for i in range(j,len(index)):
    #     if index[i - 1] + 1 != index[i]:
    #         dataIndex.append(index[i-1])
    # for i in range(j, len(string)):
    #     if string[i - 1] + 1 != string[i]:
    #         dataString.append(string[i-1])
    #             # res = res + strA[index[i - 1]:index[i]]
    #     # data.append(res)
    # print(dataIndex)
    # print(dataString)
    # resultIndex = []
# ======================================================
# import sys
# # 用来判断坐标是否合法
# def check_valid(mg, x, y):
#     if x >= 0 and x < len(mg) and y >= 0 and y < len(mg[0]) \
#             and mg[x][y] == 1:
#         return True
#     else:
#         return False
#
#
# # 迷宫结果优化
# def process(step):
#     # 先识别哪些无路可走的点的下一个点
#     change_records = []
#     for i in range(len(step) - 1):
#         if (abs(step[i][0] - step[i + 1][0]) == 0 and abs(step[i][1] - step[i + 1][1]) == 1) or \
#                 (abs(step[i][0] - step[i + 1][0]) == 1 and abs(step[i][1] - step[i + 1][1]) == 0):
#             pass
#         else:
#             change_records.append(i + 1)
#     print(change_records)
#
#     # 然后根据这些点识别出这个点的最远回退点
#     clip_nums = []
#     for i in change_records:
#         for j in range(i):
#             if (abs(step[j][0] - step[i][0]) == 0 and abs(step[j][1] - step[i][1]) == 1) or \
#                     (abs(step[j][0] - step[i][0]) == 1 and abs(step[j][1] - step[i][1]) == 0):
#                 break
#             clip_nums.append((j, i))
#     print(clip_nums)
#
#     # 注意回退点之间的包含关系, 逆序处理, 是为了规避顺序对列表进行处理后下标偏移的问题
#     record = []
#     for i in clip_nums[::-1]:
#         if not (i[0] in record or i[1] in record):
#             step = step[:i[0] + 1] + step[i[1]:]
#         record += list(range(i[0], i[1]))
#     print(step)
#
#
# step = []
# n = 6
#
# def walk(mg, x, y):
#     global step
#     if x == 5 and y == 5:
#         step.append((x, y))
#         process(step)
#         print("Walk success!")
#         sys.exit()
#
#     if check_valid(mg, x, y):
#         step.append((x, y))
#         mg[x][y] = 2
#         walk(mg, x, y + 1)
#         walk(mg, x + 1, y)
#
#
# mg = [[1, 0, 0, 1, 1, 0],
#       [1, 1, 0, 0, 0, 1],
#       [0, 0, 0, 1, 0, 1],
#       [0, 1, 1, 1, 0, 1],
#       [0, 1, 0, 1, 0, 1],
#       [1, 1, 1, 0, 0, 0]]
#
# walk(mg, 0, 0)  # 从5, 0这个点开始走迷宫, 出口为0, 0
# =================================================
#
# import sys
# if __name__ == '__main__':
#     number = int(input())
#     for i in range(number):
#         n = int(input())
#         x = []
#         y = []
#         resX = []
#         resY = []
#         for i in range(n):
#             data = sys.stdin.readline().strip().split()
#             x.append(int(data[0]))
#             y.append(int(data[1]))
#             resX.append(int(data[0]))
#             resY.append(int(data[1]))
#         for i in range(len(x)):
#             for j in range(len(y)):
#                 if x[i] == y[j] and i != j:
#                     resX.remove(x[i])
#                     resY.remove(y[j])
#                     break
#         if len(resX) <= 1 and len(resY) <= 1:
#             print("yes")
#         else:
#             print("no")
# =======================================================
# import sys
#
# def getNum(data, index, a):
#     if data[index - 1] > data[index]:
#         k = data.index(data[index])
#         data.pop(k)
#         a = a + 1
#     if data[index] > data[index + 1]:
#         k = data.index(data[index])
#         data.pop(k)
#         a = a + 1
#     return a
#
# if __name__ == '__main__':
#     num = int(sys.stdin.readline().strip())
#     content = sys.stdin.readline().strip().split()
#     data = []
#     for i in range(len(content)):
#         data.append(int(content[i]))
#     s = 0
#     for i in range(1, len(content) - 1):
#         s = s + getNum(data, i, 0)
#
#     print(s)
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        List<int[]> numList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int[] num = new int[3];
            num[0] = scan.nextInt();
            num[1] = scan.nextInt();
            num[2] = scan.nextInt();
            numList.add(num);
        }
        int count=0;
        for (int i = 0; i < n; i++) {
            int[] tmp = numList.get(i);
            for (int j = 0; j < n; j++) {
                if(compareThem(tmp,numList.get(j))){
                    count++;
                    break;
                }
            }
        }
        System.out.println(count);
    }

    private static boolean compareThem(int[] tmp, int[] ints) {
        if(tmp[0]<ints[0] && tmp[1]<ints[1] && tmp[2]<ints[2])
            return true;
        return false;
    }
}