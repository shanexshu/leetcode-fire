class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        left = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr>=target:
                ans = min(ans, i-left+1)
                curr -= nums[left]
                left += 1
        
        if ans>len(nums): return 0
        return ans
        