from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        sliding window
        keep track of max count of a character
        '''
        left = 0
        maxCount = 0
        counts = defaultdict(int)
        ans = 0
        
        for right in range(len(s)):
            c = s[right]
            counts[c] += 1
            maxCount = max(counts[c], maxCount)
            
            # diff between len and maxCount is the num of replacements neeeded
            while right-left+1-maxCount>k:
                counts[s[left]] -= 1
                left += 1
        
            ans = max(ans, right-left+1)
        
        return ans
'''
sliding window

AACABAAAA
 l
    r


k 1
maxcount 3
len 4
'''