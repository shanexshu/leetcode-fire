class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combo = []
        self.ans = []
        
        def backtrack(i, target):
            # base case: if target==0, we're done. 
            if target == 0 and self.combo:
                self.ans.append(self.combo[:])
                return

            # recurrence: ans = cand_i + ans(target-cand_i)

            for c_i in range(i, len(candidates)):
                c = candidates[c_i]
                if target>=c:
                    self.combo.append(c)
                    backtrack(c_i, target-c)
                    self.combo.pop()
            
        backtrack(0, target)
        return self.ans