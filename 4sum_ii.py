class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        ans = 0
        
        sums_12 = defaultdict(int)
        for x in nums1:
            for y in nums2:
                sums_12[x+y] += 1
                
        for x in nums3:
            for y in nums4:
                ans += sums_12[-(x+y)]
                    
        return ans