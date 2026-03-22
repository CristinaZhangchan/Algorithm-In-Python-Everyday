class Solution:
    def firstMissPos(self, nums):
        nums = [n for n in nums if n > 0]
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        return target
            
nums = [0,2,3,5,7,8,9,11,12]
solution = Solution()
print(solution.firstMissPos(nums))