class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            while right>i and nums[i]==2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            while left<i and nums[i]==0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        