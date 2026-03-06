class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        resultMax =[]
        sum = 0
        resultMin =[]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k =len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if target == sum:
                    return sum
                elif target > sum:
                    resultMin.append(sum)
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                else:
                    resultMax.append(sum)
                    k -= 1
        resultMin.sort()
        resultMax.sort()
        sum = min(abs(resultMin[-1] - target), abs(resultMax[0] - target))
        return sum

nums = [-1,2,1,-4,4,12,5,1,5]
target = 5
solution = Solution()
print(solution.threeSumClosest(nums, target))  
