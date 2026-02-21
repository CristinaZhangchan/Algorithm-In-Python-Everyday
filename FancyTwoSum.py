# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have several solutions, and you may not use the same element twice.
#You can return the answer in any order.
class Solution:
    def twoSum(self, nums, target):
        list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    list.append([i,j])

        return list


input = [2, 7, 11, 15, 2, 4,5,5,5,4,4 ]
target = 9
solution = Solution()
print(solution.twoSum(input, target))  