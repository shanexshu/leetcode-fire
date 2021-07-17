class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0
        numset = set(nums)
        for num in nums:
            if num-1 not in numset:
                curr = 1
                while num+1 in numset:
                    curr += 1
                    num += 1
                ans = max(ans, curr)
                
        return ans