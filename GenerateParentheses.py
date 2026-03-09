class Solution:
    def generateParenthese(self, n):
        sol, ans = [], []
        def backtrack(openn,closen):
            if len(sol) == 2 * n:
                ans.append(''.join(sol))
                return

            if openn < n:
                sol.append('(')
                backtrack(openn+1, closen)
                sol.pop()

            if openn > closen:
                sol.append(')')
                backtrack(openn, closen+1)
                sol.pop()
        
        backtrack(0,0)
        return ans
    
n = 4
solution = Solution()
print(solution.generateParenthese(n))

