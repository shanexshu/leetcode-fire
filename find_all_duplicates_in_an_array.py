class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]<0:
                ans.append(abs(nums[i]))
            nums[index] *= -1
        return ans