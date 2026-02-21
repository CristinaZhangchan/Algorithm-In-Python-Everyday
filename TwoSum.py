class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num]=i 
        return []


input = [2, 7, 11, 15, 2, 4,5,5,5,4,4 ]
target = 11
solution = Solution()
print(solution.twoSum(input, target))  