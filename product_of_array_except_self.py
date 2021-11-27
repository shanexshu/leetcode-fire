class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        for num in nums:
            if num==0:
                zeros+=1
                if zeros>1: return [0]*len(nums)
            else:
                prod *= num
                
        if zeros==1:
            return [0 if num!=0 else prod for num in nums]
        
        return [prod//num for num in nums]