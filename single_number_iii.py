class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            if dic[num]==2:
                del dic[num]
        return dic.keys()