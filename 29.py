class Solution:
    def divideTwoIntegers(self, dividend, divisor):
        if divisor == 0 or dividend == -2**31 and divisor == -1:
            return (2**31) - 1
        quotient = abs(dividend) // abs(divisor)
        if (dividend < 0) ^ (divisor < 0):
            return -quotient
        else:
            return quotient

dividend = 7 
divisor = -3
solution = Solution()
print(solution.divideTwoIntegers(dividend, divisor))