class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def trackback(cur, pos, target):
            if target == 0:
               res.append(cur.copy())
            if target <= 0:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                trackback(cur, i+1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        trackback([],0,target)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))