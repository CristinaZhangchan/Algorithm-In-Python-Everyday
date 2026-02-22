class Solution:
    def maxArea(self, height):
        area = 0
        res = 0        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                min_con = min(height[i],height[j])
                area = min_con * (j-i)
                res = max(res, area)
        return res

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))