class Solution:
    def searchRange(self, nums, target):
        nums.sort()

        if not nums:
            return [-1, -1]
        
        i = 0       
        j = len(nums)-1
        while i <= j:
            if nums[i] == target and nums[j] == target :
                return [i,j]
            
            if nums[i] < target:
                i += 1
            elif nums[i] > target:
                return [-1,-1]
            
            if nums[j]> target:
                j -= 1
            elif nums[j] < target:
                return[-1,-1]

        return [-1,-1]
nums = [5,7,7,8,10]
target = 8
solution = Solution()
print(solution.searchRange(nums, target))