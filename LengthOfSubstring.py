class Solution:
    def lengthofLongestSubstring(self, s):
        char_set = set()
        left = max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length
    
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        max_length = 0
        current = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in char_set:
                    max_length = max(max_length,current)
                    current = 0
                    char_set.clear()
                    break
                char_set.add(s[j])
                current += 1
        return max(max_length, current)

s ="pewwkew"
solution = Solution()
print(solution.lengthofLongestSubstring(s))
            



