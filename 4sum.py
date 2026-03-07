class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        lens = len(nums)
        total = 0 
        
        for i in range(lens - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for k in range(lens-1, i+2, -1):
                if k < lens -1 and nums[k] ==nums[k-1]:
                    continue

                j = i+1
                n = k - 1
                while j < n:
                    total = nums[i]+nums[j]+nums[n]+nums[k]
                    if total == target:
                        result.append([nums[i],nums[j],nums[n],nums[k]])
                        while j < n and nums[j] == nums[j+1]: j += 1
                        while j < n and nums[n] == nums[n-1]: n -= 1
                        j += 1
                        n -= 1
                    elif total < target:
                        j += 1
                    else:
                        n -= 1
        return result

nums = [1,0,-1,0,-2,2]
target = 0
solution = Solution()
print(solution.fourSum(nums, target))