class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = math.inf
        
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if target-curr_sum==0:
                    return target
                
                if abs(target - curr_sum) < abs(ans - target):
                    ans = curr_sum
                    
                if target<curr_sum:
                    right -= 1
                else:
                    left += 1
        
        return ans