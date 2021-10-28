class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        ans = []
        if len(nums)<3: return []
        nums.sort()
        seen = set()
        for i in range(len(nums)-2):
            dic = {}
            for j in range(i+1, len(nums)):
                if dic.get(-(nums[i] + nums[j]), 0) > 0:
                    trip = [nums[i], nums[j], -(nums[i] + nums[j])]
                    if not ans or tuple(trip) not in seen:
                        ans.append(trip)
                        seen.add(tuple(trip))
                dic[nums[j]] = dic.get(nums[j], 0) + 1
            
        return ans