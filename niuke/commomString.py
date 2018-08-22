def partition(suffix_array, start, end):
    if end <= start:
        return
    index1, index2 = start, end
    base = suffix_array[start]
    while index1 < index2 and suffix_array[index2] >= base:
        index2 -= 1
    suffix_array[index1] = suffix_array[index2]
    while index1 < index2 and suffix_array[index1] <= base:
        index1 += 1
    suffix_array[index2] = suffix_array[index1]
    suffix_array[index1] = base
    partition(suffix_array, start, index1 - 1)
    partition(suffix_array, index1 + 1, end)

def find_common_string(str1, str2):
    if not str1 or not str2:
        return 0, ''
    index1, index2 = 0, 0
    length, comm_substr = 0, ''
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] == str2[index2]:
            length += 1
            comm_substr += str1[index1]
        else:
            break
        index1 += 1
        index2 += 1
    return length, comm_substr

def find_longest_repeating_strings(string):
    if not string:
        return None, None
    suffix_array = []
    # first, get the suffix arrays
    length = len(string)
    for i in range(length):
        suffix_array.append(string[i:])
    # second, sort suffix array
    start, end = 0, len(suffix_array) - 1
    partition(suffix_array, start, end)
    # third, get the longest repeating substring
    max_length,  repeat_substring = 0, ''
    for i in range(len(suffix_array) - 1):
        common_len, common_substring = find_common_string(suffix_array[i], suffix_array[i+1])
        if common_len > max_length:
            max_length, repeat_substring = common_len, common_substring
    return max_length, repeat_substring

import sys
if __name__ == "__main__":
    inputString = sys.stdin.readline()
    length, substr = find_longest_repeating_strings(inputString)
    if length == 0:
        print(" " + str(length))
    else:
        print(substr + " " + str(length))

# !usr/binenv python
# encoding:utf-8

# def slice(num_str, w):
#     result_list = []
#     for i in range(len(num_str) - w + 1):
#         result_list.append(num_str[i:i + w])
#     return result_list
#
# def get_repeat_num_seq(num_str):
#     result_dict = {}
#     result_list = []
#     for i in range(2, len(num_str)):
#         one_list = slice(num_str, i)
#         result_list += one_list
#     for i in range(len(result_list)):
#         if result_list[i] in result_dict:
#             result_dict[result_list[i]] += 1
#         else:
#             result_dict[result_list[i]] = 1
#     sorted_result_dict = sorted(result_dict.items(), key=lambda e: e[1], reverse=True)
#     return sorted_result_dict[0:10]
#
# import sys
# if __name__ == '__main__':
#     inputString = sys.stdin.readline()
#     num_list = get_repeat_num_seq(inputString)
#     result = ""
#     length = 0
#     strList = []
#     for i, num in enumerate(num_list):
#         if num[1] >= 2:
#             strList.append(num_list[i][0])
#     strList.sort(key=lambda x: len(x))
#     if len(strList) > 0 and len(strList[-1]) >= 4:
#         for i in range(len(strList)):
#             if len(strList[i]) == len(strList[-1]):
#                 result = strList[i]
#                 break
#         print(result + " " + str(len(result)))
#     else:
#         print(" 0")