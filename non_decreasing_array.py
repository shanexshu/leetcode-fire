class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if changed>0: return False
                changed += 1
                
                # case 1 - end of sequence
                if i+2==len(nums): return True
                
                # case 2 - can delete i+1
                if nums[i]<=nums[i+2]: continue
                
                # case 3 - start of sequence
                if i==0: continue
                    
                # case 4 - can delete i
                if nums[i-1]<=nums[i+1]: continue
                
                return False
                
        return True