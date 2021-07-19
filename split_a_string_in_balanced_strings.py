class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        ans = 0
        for i in range(len(s)):
            if s[i]=='R':
                l_count -= 1
            else:
                l_count += 1
            if l_count == 0:
                ans += 1
                
        return ans