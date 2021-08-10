class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # get total counts of each
        # try each index as the partition between 0s and 1s
        
        ans = len(s)
        counts_right = Counter(s)
        counts_left = Counter()
        for i in range(len(s)+1):
            ans = min(ans, counts_left.get('1',0) + counts_right.get('0',0))
            if i < len(s):
                counts_left[s[i]] += 1
                counts_right[s[i]] -= 1
        
        return ans
        