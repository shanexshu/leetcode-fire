class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use DP and keep the max and min
        n = len(nums)
        mins = [math.inf] * n
        maxes = [-math.inf] * n
        mins[0] = maxes[0] = nums[0]
        ans = nums[0]
        
        for i in range(1, n):
            mins[i] = min(mins[i-1]*nums[i], maxes[i-1]*nums[i], nums[i])
            maxes[i] = max(maxes[i-1]*nums[i], mins[i-1]*nums[i], nums[i])
            ans = max(ans, maxes[i])
        
        return ans
