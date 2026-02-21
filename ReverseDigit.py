class Solution:
    def reverseDigit(self, s):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        sign=-1 if s < 0 else 1
        s = abs(s)
        res = 0

        while s:
            digit = s % 10
            s //=10
            
            if res > (INT_MAX - digit) // 10:
                return 0
            res = res*10 +digit
        return res * sign


num = -532435
solution = Solution()
print(solution.reverseDigit(num))