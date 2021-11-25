class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = nums[0]
        ans = currSum
        
        for i in range(1, n):
            currSum = max(nums[i], currSum + nums[i])
            ans = max(ans, currSum)
            
        return ans