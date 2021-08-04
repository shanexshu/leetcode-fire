class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        if n == 0: return 0

        # base case
        dp[0] = nums[0]

        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            ans = max(ans, dp[i])

        return ans