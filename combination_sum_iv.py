class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {}
        self.ans = 0
        
        def combo(target):
            if target in self.memo:
                return self.memo[target]
            if target<0: return 0
            if target==0: return 1
            tot = 0
            for num in nums:
                temp = combo(target-num)
                self.memo[target-num] = temp
                tot += temp
            self.memo[target] = tot
            return tot
        
        return combo(target)