# ===================================================
# 大富翁游戏:
# 玩家根据骰子的点数决定走的步数，即骰子点数为1时可以走一步，
# 点数为2时可以走两步，点数为n时可以走n步。求玩家走到第n步
# （n<=骰子最大点数且是方法的唯一入参）时，总共有多少种投骰子的方法。

# 它由f(n-1),f(n-2),f(n-3)….f(1)分别到f(n)的总和组成
# def getNumber(n):
#     result = 0
#     if n == 1:
#         result = 1
#     elif n == 2:
#         result = 2
#     else:
#         for i in range(1, n):
#             result = result + getNumber(n - i)
#         result = result + 1
#     return result
# n = int(input())
# print(getNumber(n))
# ===================================================
# import sys
# if __name__ == '__main__':
#     n = int(input())
#     numsA = sys.stdin.readline().strip().split()
#     numsB = sys.stdin.readline().strip().split()
#     resultList = []
#     numsC = []
#     for i in range(0, n):
#         for j in range(n - 1, -1, -1):
#             if i < j and numsB.index(numsB[i]) < numsB.index(numsB[j]) and numsA.index(numsB[i]) > numsB.index(numsB[j]):
#                 resultList.append(numsB[i])
#                 resultList.append(numsB[j])
#     numsC.append(resultList[0])
#     numsC.append(resultList[1])
#     for i in range(2, n - 2, 2):
#         if resultList[i] == resultList[i - 1] and resultList[i + 1] not in numsC:
#             numsC.append(resultList[i + 1])
#     print(len(numsC))
# ===================================================
# 面积包含
# import java.util.Scanner;
#
# public
#
#
# class fun1 {
# public static void main(String[] args) {
# Scanner sc = new Scanner(System.in );
# int n = Integer.valueOf(sc.nextLine());
# int left = 0, right = 0, up = 0, down = 0;
# for (int i = 0; i < n; i++) {
# String[] s = sc.nextLine().split(" ");
# int x = Integer.valueOf(s[0]);
# int y = Integer.valueOf(s[1]);
# if (i == 0) {
# left = x;
# right = x;
# up = y;
# down = y;
# }
# else {
# left = Math.min(left, x);
# right = Math.max(right, x);
# up = Math.max(up, y);
# down = Math.min(down, y);
# }
# }
# long max = Math.max(right-left, up - down);
# System.out.println(max * max);
#
# }
# }


