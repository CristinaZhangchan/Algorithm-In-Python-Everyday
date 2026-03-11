class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            # 只要当前数字 >= target，i 就是插入点
            if nums[i] >= target:
                return i
        # 如果循环走完都没返回，说明 target 应该排在最后
        return len(nums)

nums = [1,3,5,6]
target = 2
solution = Solution()
print(solution.searchInsert(nums, target))