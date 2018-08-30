import sys

def getList(index, myList):
    result = []

    return result
if __name__ == '__main__':
    number = int(input())
    for i in range(number):
        n = int(sys.stdin.readline().strip())
        arrayList = []
        for i in range(n):
            arrayList.append(sys.stdin.readline().strip())
        result = []
        for i in range(len(arrayList[0])):
            result.append("".join(getList(i, arrayList[0])))
        dataResult = []
        for i in range(len(result)):
            dataResult.append(result[i][0:len(arrayList[0])])
            dataResult.append(result[i][len(arrayList[0]):len(result[i])])
        for i in range(1, n):
            if arrayList[i] in dataResult:
                print("Yeah")
                break
            else:
                print("Sad")
                break