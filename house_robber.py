class Solution:
    def rob(self, nums: List[int]) -> int:
        # keep a dp array that holds the max value of robbing houses up to and including i
        # for dp[i], value is max of dp[i-1] and dp[i-2]+nums[i]
        
        if not nums: return 0
        if len(nums)<3:
            return max(nums)
        
        dp = [nums[0]]*len(nums)
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]
    
    
    # 1,2,3,1
    # dp = 1,2,4,4
    
    #      2,7,9,3,1
    # dp = 2,7,11,11,12