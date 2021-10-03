class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i>farthest: return False
            if i==len(nums)-1: return True
            farthest = max(farthest, i+nums[i])
        return False