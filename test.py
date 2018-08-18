class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # indexList = []
        # for index, val in  enumerate(nums):
        #     number = target - val
        #     if number in nums:
        #         indexList.append(index)
        # return indexList

        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums[i + 1:]:
                return [i, nums.index(pair, i + 1)]
        return None

nums = [1,2,3,4,5,6,7,8,20,30]

target = 5

re = Solution()

result = re.twoSum(nums, target)

print(result)
