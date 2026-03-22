class Solution:
    def permutation(self, nums):
        res = []
        def trackback(cur):
            if cur == len(nums):
                res.append(nums[:])

            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i],nums[cur]
                trackback (cur+1)
                nums[cur], nums[i] = nums[i],nums[cur]
        trackback(0)
        return res
nums = [1,2,3]
solution = Solution()
print(solution.permutation(nums))