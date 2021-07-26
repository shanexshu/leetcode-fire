from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        counts = Counter()
        for num in nums:
            ans += counts[num]
            counts[num] += 1
        return ans
        
'''
naive O(n^2)
two for loops

O(n)
count freq of each num
2 -> 1
3 -> 1+2 = 3
1,1,1 (1+1)
4 -> 6
1,1,1,1 (3+2+1)
5 -> 4+3+2+1

n -> (n-1)*(n)/2
1,1,1,1,1

1) loop through once to count, then loop through counts
2) 

'''