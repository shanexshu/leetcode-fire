class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for i in reversed(range(2, len(nums))):
            left = 0
            right = i-1
            while left<right:
                if nums[left]+nums[right] > nums[i]:
                    ans += right-left    # if works with left, right, i then it works with left being anything in between
                    right -= 1
                else:
                    left += 1
        
        return ans