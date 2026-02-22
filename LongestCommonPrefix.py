class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i >= len(j) or j[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    
strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
