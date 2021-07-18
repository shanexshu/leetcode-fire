class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}  # store the index where last seen
        ans = 0
        for i in range(len(s)):
            if s[i] in seen:
                left = max(left, seen[s[i]] + 1)
            ans = max(ans, i-left+1)
            seen[s[i]] = i
            
        return ans
                
        
        # pwwkew
        #    l 
        #      i
        # seen: {kew}
        # ans = 1