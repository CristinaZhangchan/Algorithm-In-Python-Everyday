class Solution:
    def removeDuplicate(self,nums):
        i = 1
        for j in range(len(nums)-1):
            if nums[j]!=nums[j+1]:
                nums[i]=nums[j]
                i +=1
        return i



nums = [0,0,1,1,1,2,2,3,3,4,5,7,8,9]
solution = Solution()
print(solution.removeDuplicate(nums))