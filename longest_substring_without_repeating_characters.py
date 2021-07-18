class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        ans = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1
            ans = max(ans, i-left+1)
            seen.add(s[i])
            
        return ans
                
        
        # pwwkew
        #    l 
        #      i
        # seen: {kew}
        # ans = 1