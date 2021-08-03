class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subs = set()
        subs.add(())
        nums.sort()
        
        for num in nums:
            curr_subs = subs.copy()
            for sub in curr_subs:
                newsub = sub + (num,)
                subs.add(newsub)
                
        return [list(sub) for sub in subs]